<template>
    <NavBar />
    <form class="search-box" @submit.prevent="search()">

            <input type="text" v-model="target">

            <button class="search-button">Search</button>

             </form>
    <div v-if="recipes.length" class="gallery">
        <div v-for="recipe in recipes" :key="recipe.id">
            <div class="card">
                <img :src="recipe.photo" alt="">
                <div class="info-recipe">
                    <router-link :to="{ name: 'recipesDetails', params: { id: recipe.id} }">
                        <h2>{{ recipe.title }}</h2>
                    </router-link>

                    <p><span class="field">Category: </span><span class="value">{{ recipe.category }}</span></p>
                    <p><span class="field">Ingredients: </span><span class="value">{{ recipe.ingredients }}</span></p>
                    <p><span class="field">Time: </span><span class="value">{{ recipe.time_in_minutes}} min</span></p>
                    <p><span class="field">author: </span><span class="value">{{ recipe.author }}</span></p>
                    <p><span class="field">Published: </span><span class="value">{{ recipe.publication_date.split('T')[0]}}</span></p>
                </div>
            </div>
        </div>
    </div>
    <div class="page-buttons">
        <button class="button is-light" @click="goToNextPage()" v-if="showNextButton">Next</button>
        <button class="button is-light" @click="goToPreviousPage()" v-if="showPreviousButton">Previous</button>
    </div>
</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";

export default {
    components: { NavBar },
    data() {
        return {
            recipes: [],
            showNextButton: false,
            showPreviousButton: false,
            currentPage: 1,
            target:''
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

            axios.get(`/recipes/?page=${this.currentPage}&search=${this.target}`)
            .then(response => {
                this.recipes = response.data.results

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
            console.log(this.target)
            this.getAllRecipes()
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
span.field{
    font-style: italic;
    text-transform: lowercase;
    background: darkgrey;
    color: white;
    border-radius: 4px;
    padding: 2px 8px;
    margin-right: 6px;
}
span.value {
     letter-spacing: 1px;
     font-size: 18px;
     font-weight: bold;
}
.search-box {
    padding: 0;
    display: flex;
}
.search-button{
    margin-top: 0;
}
.gallery {
    margin: 60px auto;
    width: 900px;

}
.card {
    display: flex;
    border-radius: 4px;
    background: white;
    margin-bottom: 2px;

}
.card img{
    height: 300px;
    border-radius: 0 28px 28px 0;
    border: 5px white solid;
}
.card .info-recipe {
    text-align: left;
    margin-left: 20px;

}
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

</style>