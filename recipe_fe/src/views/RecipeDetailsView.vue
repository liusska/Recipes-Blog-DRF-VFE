<template>
    <NavBar />
<div v-if="recipe">
    <h1> {{ recipe.title }} </h1>

    <div class="container">
        <div class="recipe-info">
            <div>
                <img v-if="recipe.photo !==''" class="details-img" :src="recipe.photo" alt="">
                <img v-else class="details-img"  src="data:image/png;base64,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"  alt="">

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
            console.log(formData)
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