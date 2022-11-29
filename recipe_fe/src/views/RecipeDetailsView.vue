<template>
    <NavBar />
<div v-if="recipe">
    <h1> {{ recipe.title }} </h1>

    <div class="container">
        <div class="recipe-info">
            <div>
                <img v-if="recipe.photo !== null" class="details-img" :src="recipe.photo" alt="">
                <img v-else class="details-img" src="http://127.0.0.1:8000/media/recipes/default-food-image.jpg">
            </div>
            <div class="info">
                <p><span class="field">Category: </span><span class="value">{{ recipe.category }}</span></p>
                <p><span class="field">Ingredients: </span><span class="value">{{ recipe.ingredients }}</span></p>
                <p><span class="field">Time: </span><span class="value">{{ recipe.time_in_minutes}} min</span></p>
                <p><span class="field">author: </span><span class="value">{{ recipe.author }}</span></p>
                <p><span class="date">
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
        <h2>Recipe Description: </h2>
        <p class="recipe-desc-text">{{ recipe.description}}</p>
    </div>
    <div v-if="trailer_url !== null">
        <iframe width="590" height="400" :src="trailer_url"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen></iframe>
    </div>
    <div class="comment-container">
        <div class="comments-box" v-if="comments.length">
            <h3>Comments:</h3>
            <div class="comment" v-for="comment in comments" :key="comment.id">
                <table class="comments-table">
                    <tr>
                        <td><p><span>{{comment.username}}</span></p></td>
                        <td><p>{{comment.comment}}</p></td>
                        <td><p class="date">
                            {{comment.publication_date.split('T')[0]}}
                            {{ (comment.publication_date.split('T')[1]).split('.')[0]}}
                        </p></td>
                    </tr>
                </table>
            </div>

        </div>
        <form class="comment-form" @submit.prevent="commentRecipe()">
            <input type="text" v-model="new_comment" placeholder="Add your comment here...">
            <button class="comment-form-button">comment</button>
        </form>
    </div>
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
            trailer_url: null,
            currentUser: null,
            currentUserId:null,
            author: null,
            new_comment: '',
            comments: [],
        }
    },
    mounted() {
        this.getRecipeDetails()
    },
    methods: {
        async getRecipeDetails(){
            await axios.get(`/recipes/${this.id}`)
                .then(response => {
                    this.recipe = response.data
                    this.author = response.data.author
                    if (this.recipe.video !== this.recipe.photo){
                        this.trailer_url="https://www.youtube.com/embed/" + this.recipe.video.split('=')[1]
                    }
                })
                .catch(err => console.log(err.messages))
                this.getCurrentUser()
                this.getAllRecipeComments()
        },

        getCurrentUser(){
            axios.get('/auth/login/')
            .then(response => {
                this.currentUser = response.data.user
                this.currentUserId = response.data.user_id
            })
            .catch(err => console.log(err.messages))
        },

        commentRecipe(){
             const formData = {
                 recipe: this.recipe.id,
                 user: this.currentUserId,
                 comment: this.new_comment
            }
            axios.post('/comments/', formData)

            this.getRecipeDetails()
            this.new_comment=''
        },

        getAllRecipeComments(){
            axios.get('/comments/')
            .then(response => {
                let recipes = response.data
                this.comments = recipes.filter(post => post.recipe === this.recipe.id)
            })
            .catch(err => console.log(err.messages))
        }
    },
}
</script>

<style>

h1 {
    margin-bottom: 40px;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: bold;
    font-size: 42px;
    color: dimgrey;
    padding-top: 20px;
    padding-bottom: 40px;
}


.comments-table{
    margin: 5px auto;
    background: white;
    border-top-left-radius: 20px;
    border-bottom-right-radius: 20px;
}
.comment-form-button {
    margin: 5px 150px;
    background: cornflowerblue;
    text-transform: uppercase;
}

.comment-form {
    padding-bottom: 0;
}
.comment-form input::placeholder{
    font-style: italic;
}

.comments-table p{
    font-style: italic ;
}

.comments-table p span{
    font-weight: bold ;
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

.date{
    font-size: 12px;
}

.info{
    margin-top: 30px;
    margin-left: 20px;
}

.recipe-info {
    display: flex;
    padding-right: 36px;
}

.recipe-info p {
    text-align: left;
    padding-left: 20px;
}
.recipe-desc-text{
    font-size: 22px;
    padding: 20px 50px;
    margin: 2px 70px;
    color: slategray;
}
.recipe-description h2{
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 60px;
    color: slategray;
}
span.field{
    font-style: italic;
    text-transform: lowercase;
    background: darkgrey;
    color: white;
    font-size: 15px;
    border-radius: 4px;
    padding: 4px 8px;
    margin-right: 6px;
}
span.value {
    letter-spacing: 1px;
    font-size: 18px;
    font-weight: bold;
    color: darkslategray;

}
</style>