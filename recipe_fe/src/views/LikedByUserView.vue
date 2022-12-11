<template>
    <NavBar/>
    <h1><span class="username-field">{{ user }}</span> 's Favorite Posts</h1>
    <div v-if="recipes.length" class="gallery">
        <RecipesPost
            v-for="recipe in recipes"
            :key="recipe.id"
            :recipe="recipe"
        />
    </div>

    <h1 v-else>*** No content yet ***</h1>
    <div class="page-buttons">
        <button class="button is-primary" @click="goToNextPage()" v-if="showNextButton">view more</button>
        <button class="button is-danger" @click="goToTopPage()" v-if="goToTopPageButton">go to top</button>

    </div>
    <div>
        <Footer/>
    </div>

</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";
import RecipesPost from "@/components/RecipesPost";
import Footer from "@/components/Footer";

export default {
    name: "LikedByUserView",
    components: { NavBar, RecipesPost, Footer },
    data() {
        return {
            recipes: [],
            target: '',
            user: null,
            register_date: '',
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
            this.getUserFavoriteRecipes()
        },
        goToTopPage() {
            this.recipes = []
            this.currentPage = 1
            this.getUserFavoriteRecipes()
        },
        getCurrentUser() {
            document.title = 'Favorite | Recipe Blog'

            axios
                .get('/auth/login/')
                .then(response => {
                    this.user = response.data.user
                    this.register_date = response.data.register_date
                })
                .catch(error => {
                    console.log(error)
                })
            this.getUserFavoriteRecipes()
        },
        getUserFavoriteRecipes() {
            axios.get(`/auth/liked/`)
                .then(response => {
                    const userRecipes = response.data.results
                    for (let recipeIndex in userRecipes) {
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
                    console.log(recipe)
                    recipe["avgRate"] = response.data.avg_rating
                    this.recipes.push(recipe)
                })
                .catch(err => console.log(err.messages))
        },
    }
}
</script>

<style scoped>
 h1 {
     font-size: 38px;
     margin-top: 30px;
 }
.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    width: 100vw;
}

select {
    width: 260px;
    height: 40px;
}

.page-buttons {
    margin: 30px auto;
}
</style>