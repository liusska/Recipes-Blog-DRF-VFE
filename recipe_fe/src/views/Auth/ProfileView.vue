<template>
    <NavBar/>
    <section class="hero is-info">
        <div class="hero-body">
            <p class="title">Hello, {{ user }}</p>
            <p class="subtitle">Date joined : {{register_date.split(' ')[0] }}</p>
        </div>

    </section>

<div class="card">
  <div class="card-content">
    <p class="title">
       <router-link to="/profile/liked" class="link-to-favorite">View Your <span>{{ favorite_count }}</span> favorite posts <i class="fa fa-heart"></i></router-link>
    </p>
  </div>
</div>


    <h2 class="info-h">Posts By <span>{{ user }}</span></h2>

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
import Footer from "@/components/Footer";
import RecipesPost from "@/components/RecipesPost";

export default {
    name: "ProfileView",
    components: {NavBar, Footer, RecipesPost},
    data() {
        return {
            recipes: [],
            target: '',
            user: null,
            register_date: '',
            currentPage: 1,
            showNextButton: false,
            goToTopPageButton: false,
            favorite_count: 0,
        }
    },
    mounted() {
        this.getCurrentUser()
        this.getUserFavoriteRecipesCount()
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
                    this.register_date = response.data.register_date
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
        getUserFavoriteRecipesCount() {
            axios.get(`/auth/liked/`)
                .then(response => {
                    this.favorite_count = response.data.count
                })
                .catch(err => console.log(err.messages))
        },
    }


}
</script>

<style scoped>
.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    width: 100vw;
}

.page-buttons {
    margin-bottom: 30px;
}

.fa.fa-heart{
    color: red;
}

.info-h {
    margin-top: 100px;
    font-size: 40px;
}

.info-h span {
    font-weight: bold;
}

</style>