<template>
    <NavBar />
    <form class="search-box" @submit.prevent="search()">
            <input type="text" v-model="target">
            <button class="search-button">Search</button>
    </form>

    <div v-if="recipes.length" class="gallery">
        <RecipesPost
            v-for="recipe in recipes"
            :key="recipe.id"
            :recipe="recipe"/>
    </div>
    <div class="page-buttons">
        <button class="button is-light" @click="goToPreviousPage()" v-if="showPreviousButton">Previous</button>
        <button class="button is-light" @click="goToNextPage()" v-if="showNextButton">Next</button>
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
            showPreviousButton: false,
            currentPage: 1,
            target:'',
            author:'',
        }
    },
    mounted() {
        this.getAllRecipes()
    },
    methods: {
        goToNextPage(){
            this.currentPage +=1
            this.getAllRecipes()
        },
        goToPreviousPage() {
            this.currentPage -= 1
            this.getAllRecipes()
        },

        getAllRecipes(){
            this.showNextButton = false
            this.showPreviousButton = false
            document.title = 'Gallery | Recipe Blog'
            axios.get(`/recipes/?page=${this.currentPage}&search=${this.target}`)
                .then(response => {
                    for (let recipe of response.data.results){
                        this.getAvgRate(recipe)
                    }

                    if (response.data.next){
                        this.showNextButton = true
                    }
                    if (response.data.previous){
                        this.showPreviousButton = true
                    }
                })
                .catch(err => console.log(err.messages))
        },
        search(){
            this.recipes = []
            this.getAllRecipes()
            this.target = ''
        },
        searchByCategory(e){
            this.target = e.target.value;
            this.recipes = []
            this.getAllRecipes()
        },
        getAvgRate(recipe) {
            axios.get(`/recipes/rate/${recipe.id}`)
                .then(response => {
                    recipe["avgRate"] = response.data.avg_rating
                    this.recipes.push(recipe)
                })
                .catch(err => console.log(err.messages))
        },
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
/*span.field{*/
/*    font-style: italic;*/
/*    text-transform: lowercase;*/
/*    background: darkgrey;*/
/*    color: white;*/
/*    border-radius: 4px;*/
/*    padding: 2px 8px;*/
/*    margin-right: 6px;*/
/*}*/
/*span.value {*/
/*     letter-spacing: 1px;*/
/*     font-size: 18px;*/
/*     font-weight: bold;*/
/*}*/
.search-box {
    padding: 0;
    display: flex;
}
.search-button{
    margin-top: 0;
}
.search-button:hover {
    cursor: pointer;
}
.gallery {
    margin: 60px 20px;
    width: 1200px;

}
/*.card {*/
/*    display: flex;*/
/*    border-radius: 4px;*/
/*    background: white;*/
/*    margin-bottom: 2px;*/
/*    width: 1100px;*/
/*}*/

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
/*.card .info-recipe {*/
/*    text-align: left;*/
/*    margin-left: 20px;*/

/*}*/
/*.info-card .avg-rate {*/
/*    font-size: 20px;*/
/*}*/

/*.info-card .fa.fa-star {*/
/*    font-size: 22px;*/
/*}*/

.info-recipe a{
    text-decoration: none;
    color: #2c3e50;
    font-size: 26px;
}
.button.is-light {
    background: darkslategrey;
    margin-top: 0;
    margin-bottom: 50px;
}
/*button.button-category{*/
/*    padding: 2px 10px;*/
/*    background: none;*/
/*    border: 1px solid darkgray;*/
/*    border-radius: 3px;*/
/*    color: black;*/
/*    font-weight: bold;*/
/*}*/
/*button.button-category:hover{*/
/*    cursor: pointer;*/
/*}*/
</style>