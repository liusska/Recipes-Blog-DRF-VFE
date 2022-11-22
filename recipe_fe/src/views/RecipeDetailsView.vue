<template>
    <NavBar />
<div v-if="recipe">
    <h1> {{ recipe.title }} </h1>

    <div class="container">
        <div class="recipe-info">
            <div>
                <img class="details-img" :src="recipe.photo" alt="">
            </div>
            <div class="info">
                <p><span class="field">Category: </span><span class="value">{{ recipe.category }}</span></p>
                <p><span class="field">Ingredients: </span><span class="value">{{ recipe.ingredients }}</span></p>
                <p><span class="field">Time: </span><span class="value">{{ recipe.time_in_minutes}} min</span></p>
                <p><span class="field">author: </span><span class="value">{{ recipe.author }}</span></p>
                <p><span class="field">Published: </span>
                    <span class="value">
                        {{recipe.publication_date.split('T')[0]}}
                        {{ (recipe.publication_date.split('T')[1]).split('.')[0]}}
                    </span></p>
                <div v-if="currentUser === author" class="buttons-container">
                    <router-link class="button edit" :to="{ name: 'edit', params: { id: recipe.id} }">Edit</router-link>
                    <router-link class="button delete" :to="{ name: 'delete', params: { id: recipe.id} }">Delete</router-link>
                </div>

            </div>

        </div>
     </div>

    <div class="recipe-description">
        <h3>Description: </h3>
        <p>{{ recipe.description}}</p>
    </div>
</div>

<div v-else>
    <p>loading job details...</p>
</div>
</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";

export default {
    props: ['id'],
    components: { NavBar },
    data() {
        return {
            recipe: null,
            currentUser: null,
            author: null,
        }
    },
    mounted() {
        this.getRecipeDetails()
    },
    methods: {
        getRecipeDetails(){
            axios.get(`/recipes/${this.id}`)
                .then(response => {
                    this.recipe = response.data
                    this.author = response.data.author
                    console.log(`author: ${response.data.author}`)
                })
            .catch(err => console.log(err.messages))
            this.getCurrentUser()
        },
        getCurrentUser(){
            axios.get('/auth/login/')
            .then(response => {
                console.log(`current user: ${response.data.user}`)
                this.currentUser = response.data.user
            })
            .catch(err => console.log(err.messages))
        }
    },
}
</script>

<style>

h1 {
    margin-bottom: 40px;
}

.details-img {
    height: 380px;
    padding-left: 200px;
}

.button {
    text-transform: uppercase;
    background: #0b6dff;
    border-radius: 4px;
    padding: 6px 12px;
    text-decoration: none;
    color: white;
}

.button.edit {
    background: green;

}

.button.delete{
    margin-left: 22px;
    background: darkred;
}

.buttons-container {
    margin-top: 40px;
}

.info{
    margin-top: 40px;
}
.recipe-info {
    display: flex;
    padding-right: 36px;
}

.recipe-info p {
    text-align: left;
    padding-left: 20px;
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
</style>