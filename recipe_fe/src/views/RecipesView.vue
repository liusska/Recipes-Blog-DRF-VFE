<template>
    <div v-if="recipes.length" class="gallery">
        <div v-for="recipe in recipes" :key="recipe.id">
            <div class="card">
                <img :src="recipe.photo" alt="">
                <div class="info-recipe">
                    <router-link :to="{ name: 'recipesDetails', params: { id: recipe.id} }">
                        <h2>{{ recipe.title }}</h2>
                    </router-link>

                    <p>Category: {{ recipe.category }}</p>
                    <p>Ingredients: {{ recipe.ingredients }}</p>
                    <p>Time: {{ recipe.time_in_minutes}} min</p>
                    <p>author: {{ recipe.author }}</p>
                    <p>Published: {{ recipe.publication_date}}</p>
                </div>
            </div>

        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            recipes: [],
        }
    },
    mounted() {
        fetch('http://127.0.0.1:8000/recipes/', {
            method: 'get',
            headers: {
                'Content-Type': 'application/json',
            }
        })
            .then((res) => res.json())
            .then(data => this.recipes = data)
            .catch(err => console.log(err.messages))
    }

}
</script>

<style>
body {
    background: whitesmoke;
}
.gallery {
    margin: 100px auto;
    width: 900px;

}
.card {
    display: flex;
    border-radius: 4px;
    background: white;
    margin-bottom: 2px;

}
.card img{
    height: 300px;
    border-radius: 0 28px 28px 0;
    border: 5px white solid;
}
.card .info-recipe {
    text-align: left;
    margin-left: 20px;

}
.info-recipe a{
    text-decoration: none;
    color: #2c3e50;
    font-size: 26px;
}

</style>