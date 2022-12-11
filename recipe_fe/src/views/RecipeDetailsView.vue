<template>
    <NavBar />
<div v-if="recipe">
    <h1> <i class="fa fa-soup"></i>{{ recipe.title }} </h1>

    <div class="container">
        <div class="recipe-info">
            <div>
                <img v-if="recipe.photo !== null" class="details-img" :src="recipe.photo" alt="">
                <img v-else class="details-img" src="http://127.0.0.1:8000/media/recipes/default-food-image.jpg">
            </div>
            <div class="info">
                <div class="rate">
                    <div>
                        <span><i class="fa fa-star"></i></span>
                        <span class="avg-rate">&nbsp;{{this.avgRate}}</span>
                    </div>
                    <div>
                        <span class="voted-count">( {{this.rateCount}} voted )</span>
                    </div>
                    <div class="rated" v-if="this.isRated === true">
                        <p>
                            <span><i>*Thank you for the rate &nbsp;</i></span>
                        </p>
                    </div>
                    <hr>

                </div>

                <p><span class="field">Category: </span><span class="value">{{ recipe.category }}</span></p>
                <p><span class="field">Time: </span><span class="value">{{ recipe.time_in_minutes}} min</span></p>
                <p><span class="field">author: </span><span class="value">{{ recipe.author }}</span></p>
                <p><span class="date">
                        {{recipe.publication_date.split('T')[0]}}
                        {{ (recipe.publication_date.split('T')[1]).split('.')[0]}}
                    </span></p>
                <div v-if="currentUser === author" class="buttons-container">
                    <router-link class="button is-info" :to="{ name: 'edit', params: { id: recipe.id} }"><i class="fa fa-edit"></i>Edit</router-link>
                    <router-link class="button is-danger" :to="{ name: 'delete', params: { id: recipe.id} }"><i class="fa fa-trash"></i>Delete</router-link>
                </div>
            </div>
            <div class="likes">
                <a href="#" class="like" @click="likeRecipe()">
                    <p v-if="isLiked === true"><i class="fa fa-heart"><span>{{likesCount}}</span></i></p>
                    <p v-else><i class="fa fa-heart-o"><span>{{likesCount}}</span></i></p>
                    <p></p>
                </a>
            </div>
        </div>
     </div>
    <div class="field" v-if="this.currentUser !== 'AnonymousUser'">
        <div class="control" v-if="this.isRated === false">
            <div class="select">
                 <form @submit.prevent="rateRecipe()">
                     <select v-model="newRate">
                        <option v-for="option in options" :value="option.value">
                        {{ option.text }}
                        </option>
                    </select>
                <button class="button is-primary">Rate</button>
            </form>
            </div>

        </div>
    </div>



    <div class="recipe-description">

        <h2>Recipe Description: </h2>
        <div class="ingredients">
            <span class="field">Ingredients: </span>
            <ul v-for="ingredient in recipe.ingredients.split(',')">
                <li><span class="value">{{ ingredient }}</span></li>
            </ul>
        </div>

        <p class="recipe-desc-text">&nbsp&nbsp&nbsp&nbsp {{ recipe.description}}</p>
    </div>
    <div v-if="trailer_url !== null">
        <iframe width="590" height="400" :src="trailer_url"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen></iframe>
    </div>
    <div>

        <div class="comments-box" v-if="comments.length">
            <h3>Comments:</h3>
            <hr>
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

        <div>
            <form class="comment-form" @submit.prevent="commentRecipe()" v-if="this.currentUser !== 'AnonymousUser'">
            <input class="input" type="text" v-model="new_comment" placeholder="Add your comment here..." rows="25">
            <button class="button is-primary">comment</button>
        </form>
        <div class="login-msg" v-else>
            <p>Please login <a href="/login">here</a> to comment</p>
        </div>
        </div>

    </div>
</div>
</template>

<script>

import axios from "axios";
import NavBar from "@/components/NavBar";
import {isRef} from "vue";

export default {
    props: ['id'],
    components: { NavBar },
    data() {
        return {
            recipe: null,
            trailer_url: null,
            likesCount: 0,
            isLiked: false,
            isRated: false,
            avgRate: 0,
            rateCount: 0,
            newRate: 1,
            currentUser: null,
            currentUserId:null,
            author: null,
            new_comment: '',
            comments: [],
            options: [
                {text: '1', value: '1'},
                {text: '2', value: '2'},
                {text: '3', value: '3'},
                {text: '4', value: '4'},
                {text: '5', value: '5'},
                {text: '6', value: '6'},
                {text: '7', value: '7'},
                {text: '8', value: '8'},
                {text: '9', value: '9'},
                {text: '10', value: '10'},
            ]
        }
    },
    mounted() {
        this.getCurrentUser()
        this.getRecipeDetails()
    },
    methods: {
        async getRecipeDetails(){
            await axios.get(`/recipes/${this.id}`)
                .then(response => {
                    document.title = response.data.title + ' | Recipes Blog'

                    this.recipe = response.data
                    this.author = response.data.author
                    if (this.recipe.video !== this.recipe.photo){
                        this.trailer_url="https://www.youtube.com/embed/" + this.recipe.video.split('=')[1]
                    }
                    document.title = this.recipe.title
                })
                .catch(err => console.log(err.messages))
                this.getCurrentUser()
                this.getAllRecipeComments()
                this.getLikesCount()
                this.getAvgRate()
        },

        getCurrentUser(){
            axios.get('/auth/login/')
            .then(response => {
                this.currentUser = response.data.user
                console.log(response.data.user)
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
        },
        getLikesCount(){
            axios.get(`/recipes/likes/${this.id}`)
                .then(response => {
                    console.log(response)
                    this.likesCount = response.data.likes_count
                    this.isLiked = response.data.is_liked

                })
        },
        likeRecipe() {
            axios.post(`/recipes/likes/${this.id}`)
                .then(response => console.log(response))
            this.getRecipeDetails()
        },
        getAvgRate() {
            axios.get(`/recipes/rate/${this.id}`)
                .then(response => {
                    console.log(response)
                    this.avgRate = response.data.avg_rating
                    this.rateCount = response.data.rating_count
                    this.isRated = response.data.is_rate
                })
        },
        rateRecipe() {
            const formData = {
                    "rate": this.newRate,
                    "user": this.currentUserId,
                    "recipe": this.id
            }
            axios.post(`/recipes/rate/${this.id}`, formData)
                .then(response => {
                    console.log(response)
                })

            this.newRate = 1
            this.getRecipeDetails()
        }

    },
}
</script>

<style scoped>
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
td {
    padding: 2px 30px;

}
tr {
    border-radius: 20px;
    border: 1px solid lightslategrey;
}
.avg-rate {
    font-size: 28px;
    font-weight: bold;
}

.input {
    width: 500px;
    height: 100px;
}

.rate {
    display: flex;
    flex-direction: column;
}
.rated {
    font-size: 12px;
    margin-left: 60px;
}

.vote-form button {
    margin: 0;
    background: #555555;
    font-weight: bold;
}

.vote-form button:hover{
    cursor: pointer;
}

.comments-table{
    margin: 5px auto;
    background: white;
    border-top-left-radius: 20px;
    border-bottom-right-radius: 20px;
}

.comment-form{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px auto 100px auto;
    width: 500px;
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
    object-fit: contain;
}

.buttons-container {
    margin-top: 40px;
}

.buttons-container i{
    padding-right: 8px;
}

.date{
    font-size: 12px;
}

.info{
    margin-top: 30px;
}

.recipe-info {
    display: flex;
    justify-content: space-evenly;
    padding-right: 36px;
}

.recipe-info p {
    text-align: left;
}
.recipe-desc-text{
    font-size: 22px;
    padding: 20px 50px;
    margin: 2px 70px;
    color: slategray;
}
.recipe-description {
    margin-bottom: 50px;
}
.recipe-description .ingredients {
    text-align: left;
    margin-top: 100px;
    margin-left: 200px;
}

.recipe-description h2{
    letter-spacing: 2px;
    text-transform: uppercase;
    font-size: 36px;
    margin-top: 100px;
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

.fa.fa-star{
    color: yellow;
    font-size: 34px;
}

.fa.fa-heart, .fa.fa-heart-o{
    color: red;
}

.fa.fa-heart span, .fa.fa-heart-o span{
    color: darkslategray;
}

.like i{
    font-size: 20.5px;
}

.login-msg p{
    padding: 20px;
    font-size: 26px;
}

.like i:hover{
    font-weight: bold;
}
.like span {
    font-size: 26px;
    padding-left: 10px;
    font-weight: bold;
}

.voted-count {
    font-size: 12px;
    font-style: italic;
}
</style>