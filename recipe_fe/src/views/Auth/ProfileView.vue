<template>
    <h1>User Recipe Posts</h1>
    <div v-if="recipes.length" class="gallery">
        <div v-for="recipe in recipes" :key="recipe.id">
            <div class="card">
                <img :src="recipe.photo" alt="">
                <div class="info-recipe">
                    <router-link :to="{ name: 'recipesDetails', params: { id: recipe.id} }">
                        <h2>{{ recipe.title }}</h2>
                    </router-link>

                    <p>Category: {{ recipe.category }}</p>
                    <p>Ingredients: {{ recipe.ingredients }}</p>
                    <p>Time: {{ recipe.time_in_minutes}} min</p>
                    <p>author: {{ recipe.author }}</p>
                    <p>Published: {{ recipe.publication_date}}</p>
                </div>
            </div>

        </div>
    </div>
    <h1 v-else>*** No content yet ***</h1>
</template>

<script>
import axios from "axios";

export default {
    name: "ProfileView",
    data() {
        return {
            recipes: [],
        }
    },
    mounted() {
        axios.get('/auth/user/')
        .then(data => this.recipes = data.data)
        .catch(err => console.log(err))
    }


}
</script>

<style>

body {
    background: whitesmoke;
}
.gallery {
    margin: 100px auto;
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

</style>