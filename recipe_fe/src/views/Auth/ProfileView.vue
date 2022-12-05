<template>
    <NavBar />

    <div v-if="recipes.length" class="gallery">
        <h1><span class="username-field">{{user}}</span> Recipe Posts</h1>
        <RecipePost
            v-for="recipe in recipes"
            :key="recipe.id"
            :recipe="recipe"/>

    </div>

    <h1 v-else>*** No content yet ***</h1>
    <div>
        <Footer />
    </div>

</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";
import Footer from "@/components/Footer";
import RecipePost from "@/components/RecipesPost";

export default {
    name: "ProfileView",
    components: { NavBar, Footer, RecipePost },
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
            document.title = 'Profile | Recipe Blog'
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
                    console.log(response.data[item])
                    this.getAvgRate(response.data[item])
                }
            })
            .catch(err => console.log(err.messages))
        },
        selectFile(){
            this.photo = this.$refs.file.files.item(0)
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
.gallery {
    margin: 40px auto;
    width: 900px;

}
img {
    padding-left: 0;
}
/*.card {*/
/*    display: flex;*/
/*    border-radius: 4px;*/
/*    background: white;*/
/*    margin-bottom: 2px;*/

/*}*/
.card img{
    height: 300px;
    border-radius: 0 28px 28px 0;
    border: 5px white solid;
}
/*.card .info-recipe {*/
/*    text-align: left;*/
/*    margin-left: 20px;*/

/*}*/
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