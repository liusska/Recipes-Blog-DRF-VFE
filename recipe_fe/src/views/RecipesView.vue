<template>
    <NavBar
        @click="refreshRecipes($event)"
    />
    <div class="search-bar">
        <form class="search-box" @submit.prevent="searchByCategory($event)">
        <label>Category:</label>
        <select v-model="target">
            <option v-for="option in options" :value="option.value">
                {{ option.text }}
            </option>
        </select>
        <button class="search-button">filter</button>
    </form>

    <form class="search-box" @submit.prevent="search()">
            <input type="text" v-model="target">
            <button class="search-button">Search</button>
    </form>
    </div>


    <div v-if="recipes.length" class="gallery">
        <RecipesPost
            v-for="recipe in recipes"
            :key="recipe.id"
            :recipe="recipe"
            @click="searchByCategory($event)"
        />
    </div>
    <div class="page-buttons">
        <button class="button is-light" @click="goToNextPage()" v-if="showNextButton">view more</button>
        <button class="button is-light" @click="goToTopPage()" v-if="goToTopPageButton">go to top</button>

    </div>
    <div>
        <Footer/>
    </div>
</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";
import Footer from "@/components/Footer";
import RecipesPost from "@/components/RecipesPost";

export default {
    components: { NavBar, Footer, RecipesPost },
    data() {
        return {
            recipes: [],
            showNextButton: false,
            goToTopPageButton: false,
            currentPage: 1,
            target: '',
            author:'',
            options: [
                {text: 'Others', value: 'Others'},
                {text: 'Dessert', value: 'Dessert'},
                {text: 'Snack', value: 'Snack'},
                {text: 'Salad', value: 'Salad'},
                {text: 'Baked', value: 'Baked'},
                {text: 'Main', value: 'Main'},
                {text: 'Pizza', value: 'Pizza'},
            ]
        }
    },
    mounted() {
        this.getAllRecipes()
    },
    methods: {
        goToNextPage() {
            this.currentPage += 1
            this.getAllRecipes()
        },
        goToTopPage() {
            this.recipes = []
            this.currentPage = 1
            this.getAllRecipes()
        },
        getAllRecipes() {
            this.showNextButton = false
            document.title = 'Gallery | Recipe Blog'
            axios.get(`/recipes/?page=${this.currentPage}&search=${this.target}`)
                .then(response => {
                    for (let recipe of response.data.results) {
                        console.log(recipe)
                        this.getAvgRate(recipe)
                    }
                    if (response.data.next) {
                        this.showNextButton = true
                        this.goToTopPageButton = false
                    } else {
                        this.goToTopPageButton = true
                        this.showNextButton = false
                    }
                })
                .catch(err => console.log(err.messages))
        },
        search() {
            this.recipes = []
            this.getAllRecipes()
            this.target = ''
        },

        getAvgRate(recipe) {
            axios.get(`/recipes/rate/${recipe.id}`)
                .then(response => {
                    recipe["avgRate"] = response.data.avg_rating
                    this.recipes.push(recipe)
                })
                .catch(err => console.log(err.messages))
        },
        searchByCategory(e) {
            if(e.target.value){
                this.target = e.target.value;
                this.recipes = []
                this.getAllRecipes()
            }
            else if (this.target !== ''){
                this.recipes = []
                this.getAllRecipes()
            }

        },
        refreshRecipes(e){
            if(e.target.textContent){
                this.target = ''
                this.recipes = []
                this.getAllRecipes()
            }
        }
    }

}
</script>

<style>
body {
    background: whitesmoke;
}
p {
    margin: 10px;
}
form label {
    margin-top: 14px;
}
.search-bar {
    display: flex;
    flex-direction: row-reverse;
    align-items: center;
    align-content: space-between;
}

.search-box {
    padding: 0;
    display: flex;
    width: 400px;
    height: 40px;
}

.search-button{
    background: dimgrey;
    margin-top: 0;
}

.search-button:hover {
    cursor: pointer;
}
.gallery {
    margin: 60px 20px;
    width: 1200px;

}
.card img{
    height: 300px;
    border-radius: 0 28px 28px 0;
    border: 5px white solid;
    object-fit: fill;
}

.card img:hover {
    width: 600px;
    height : 550px;

}

.info-recipe a{
    text-decoration: none;
    color: #2c3e50;
    font-size: 26px;
}
.button.is-light {
    background: #aaaaaa;
    margin-top: 0;
    margin-bottom: 50px;
}
.button.is-light:hover {
    cursor: pointer;
}
</style>