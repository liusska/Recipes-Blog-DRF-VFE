<template>
    <NavBar />
    <h1>Desserts</h1>
    <div v-if="recipes.length" class="gallery">
        <RecipesPost
            v-for="recipe in recipes"
            :key="recipe.id"
            :recipe="recipe"/>

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
    name: "DessertsView",
    components: { NavBar, Footer, RecipesPost },
    data() {
        return {
            recipes: [],
            target:'dessert',
            author:'',
        }
    },
    mounted() {
        this.getAllRecipes()
    },
    methods: {
        getAllRecipes(){
            document.title = 'Desserts | Recipe Blog'
            axios.get(`/recipes/?search=${this.target}`)
                .then(response => {
                    for (let recipe of response.data.results){
                        console.log(recipe)
                        this.getAvgRate(recipe)
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

<style scoped>

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

</style>