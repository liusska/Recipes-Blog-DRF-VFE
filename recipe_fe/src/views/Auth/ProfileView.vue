<template>
    <NavBar/>

    <div v-if="recipes.length" class="gallery">
        <h1><span class="username-field">{{ user }}</span> Recipe Posts</h1>
        <RecipePost
            v-for="recipe in recipes"
            :key="recipe.id"
            :recipe="recipe"
        />

    </div>

    <h1 v-else>*** No content yet ***</h1>
    <div class="page-buttons">
        <button class="button is-light" @click="goToNextPage()" v-if="showNextButton">view more</button>
        <button class="button is-light" @click="goToTopPage()" v-if="goToTopPageButton">go to top</button>

    </div>
    <div>
        <Footer/>
    </div>

</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";
import Footer from "@/components/Footer";
import RecipePost from "@/components/RecipesPost";

export default {
    name: "ProfileView",
    components: {NavBar, Footer, RecipePost},
    data() {
        return {
            recipes: [],
            target: '',
            user: null,
            currentPage: 1,
            showNextButton: false,
            goToTopPageButton: false,
        }
    },
    mounted() {
        this.getCurrentUser()
    },
    methods: {
        goToNextPage() {
            this.currentPage += 1
            this.getUserRecipes()
        },
        goToTopPage() {
            this.recipes = []
            this.currentPage = 1
            this.getUserRecipes()
        },
        getCurrentUser() {
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
        getUserRecipes() {
            axios.get(`/auth/user/?page=${this.currentPage}&search=${this.target}`)
                .then(response => {
                    const userRecipes = response.data.results
                    for (let recipeIndex in userRecipes) {
                        console.log(userRecipes[recipeIndex])
                        this.getAvgRate(userRecipes[recipeIndex])
                    }
                    if (response.data.next) {
                        this.showNextButton = true
                        this.goToTopPageButton = false
                    } else {
                        this.goToTopPageButton = true
                        this.showNextButton = false
                    }
                })
                .catch(err => console.log(err.messages))
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
.card img {
    height: 300px;
    border-radius: 0 28px 28px 0;
    border: 5px white solid;
}

/*.card .info-recipe {*/
/*    text-align: left;*/
/*    margin-left: 20px;*/

/*}*/
.info-recipe a {
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