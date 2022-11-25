<template>
    <h1>Are you sure you want to delete this post?</h1>
    <div class="gallery">
        <div class="card">
            <img :src="recipe.photo" alt="">
            <div class="info-recipe">
                <router-link :to="{ name: 'recipesDetails', params: { id: id} }">
                    <h2>{{ recipe.title }}</h2>
                </router-link>
                <p><span class="field">Category: </span><span class="value">{{ recipe.category }}</span></p>
                    <p><span class="field">Ingredients: </span><span class="value">{{ recipe.ingredients }}</span></p>
                    <p><span class="field">Time: </span><span class="value">{{ recipe.time_in_minutes}} min</span></p>
                    <p><span class="field">author: </span><span class="value">{{ recipe.author }}</span></p>
                <button class="button delete" @click="deletePost">Delete</button>
                <button class="button cancel" @click="this.$router.push('/recipes' )">cancel</button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "DeleteRecipeView",
    props: ['id'],
    data() {
        return {
            recipe: {},
        }
    },
    mounted() {
        console.log(this.id)
        axios.get(`/recipes/${this.id}`)
            .then(data => this.recipe = data.data)
            .catch(err => console.log(err.messages))
    },
    methods: {
        async deletePost(){
            await axios.delete(`/recipes/${this.id}`)
            this.$router.push('/recipes')
        }
    }

}
</script>

<style scoped>
.button.delete {
    margin-right: 24px;
}
</style>