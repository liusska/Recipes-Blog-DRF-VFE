<template>
    <NavBar />

    <div v-if="recipes.length" class="gallery">
        <h1><span class="username-field">{{user}}</span> Recipe Posts</h1>
        <div v-for="recipe in recipes" :key="recipe.id">
            <div class="card">
                <img v-if="recipe.photo !== null" :src="recipe.photo" alt="">
                <img v-else src="http://127.0.0.1:8000/media/recipes/default-food-image.jpg" alt="">

                <div class="info-recipe">
                    <router-link :to="{ name: 'recipesDetails', params: { id: recipe.id} }">
                        <h2>{{ recipe.title }}</h2>
                    </router-link>

                    <p><span class="field">Category: </span><span class="value">{{ recipe.category }}</span></p>
<!--                    <p><span class="field">Ingredients: </span><span class="value">{{ recipe.ingredients }}</span></p>-->
                    <p><span class="field">Time: </span><span class="value">{{ recipe.time_in_minutes}} min</span></p>
                    <p><span class="field">author: </span><span class="value">{{ recipe.author }}</span></p>
                    <p><span class="field">Published: </span>
                        <span class="value">
                            {{recipe.publication_date.split('T')[0]}}
                            {{ (recipe.publication_date.split('T')[1]).split('.')[0]}}
                        </span></p>
                </div>
            </div>
        </div>
    </div>

    <h1 v-else>*** No content yet ***</h1>

</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";

export default {
    name: "ProfileView",
    components: { NavBar },
    data() {
        return {
            recipes: [],
            user: null,
        }
    },
    mounted() {
        this.getCurrentUser()
    },
    methods: {
        getCurrentUser(){
             axios
                .get('/auth/login/')
                .then(response => {
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log(error)
                })
            this.getUserRecipes()
        },
        getUserRecipes(){
            axios.get(`/recipes/user/`)
            .then(response => {
                for (let item in response.data){
                    if (response.data[item].photo !== null){
                       response.data[item].photo = `http://127.0.0.1:8000${response.data[item].photo}`
                    }
                    this.recipes.push(response.data[item])
                }
            })
            .catch(err => console.log(err.messages))
        },
        selectFile(){
            this.photo = this.$refs.file.files.item(0)
        },
    }


}
</script>

<style>

body {
    background: whitesmoke;
}
.gallery {
    margin: 40px auto;
    width: 900px;

}
img {
    padding-left: 0;
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
span.username-field {
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #0b6dff;
}

</style>