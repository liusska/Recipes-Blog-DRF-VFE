<template>
    <NavBar />
    <h1 class="title">Are you sure you want to delete this post?</h1>
    <div class="card">
    <div class="card-image">
        <figure class="image is-256x256">
            <img :src="recipe.photo" alt="">
        </figure>
    </div>
    <div class="card-content">
        <router-link :to="{ name: 'recipesDetails', params: { id: id} }">
            <h2>{{ recipe.title }}</h2>
        </router-link>
        <p><span class="field">Category: </span><span class="value">{{ recipe.category }}</span></p>
        <button class="button is-danger" @click="deletePost">Delete</button>
        <button class="button is-info" @click="this.$router.push('/recipes' )">cancel</button>
    </div>
    </div>
    <Footer/>
</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";
import Footer from "@/components/Footer";

export default {
    name: "DeleteRecipeView",
    components: {NavBar, Footer},
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
h1 {
    margin-top: 120px;
}

.card{
    margin: 80px auto 80px auto;
    width: 300px;
    position: center;
}

button {
    margin: 5px;
}

</style>