<template>
    <NavBar
        @click="refreshRecipes($event)"

    />

    <div class="search-bar">
        <form class="search-box" @submit.prevent="searchByCategory($event)">
            <div class="select">
                <select v-model="target">
                    <option v-for="option in options" :value="option.value">
                        {{ option.text }}
                    </option>
                </select>
            </div>
            <button class="button is-primary">Filter by Category</button>

        </form>

        <form @submit.prevent="search()">
            <div class="search-container">
                <input class="input" type="text" v-model="target">
                <button class="button is-primary">Search</button>
            </div>

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
        <button class="button is-primary" @click="goToNextPage()" v-if="showNextButton">view more</button>
        <button class="button is-danger" @click="goToTopPage()" v-if="goToTopPageButton">go to top</button>
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

<style scoped>

.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    width: 100vw;
}

.search-bar {
    display: flex;
    margin-top: 30px;
    flex-direction: row-reverse;
    justify-content: space-evenly
}

select {
    width: 260px;
    height: 40px;
}

.search-container {
    display: flex;
}

.page-buttons {
    margin: 30px auto;
}
</style>