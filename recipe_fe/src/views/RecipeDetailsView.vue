<template>
<div v-if="recipe">
    <h1> {{ recipe.title }} </h1>

    <div class="container">
        <div class="recipe-info">
            <div>
                <img :src="recipe.photo" alt="">
            </div>
            <div>
                <p>Category: {{ recipe.category }}</p>
                <p>Ingredients: {{ recipe.ingredients }}</p>
                <p>Time: {{ recipe.time_in_minutes}} min</p>
                <p>author: {{ recipe.author }}</p>
                <p>Published: {{ recipe.publication_date}}</p>
            </div>
        </div>
     </div>

    <div class="recipe-description">
        <h3>Description: </h3>
        <p>{{ recipe.description}}</p>
    </div>
</div>

<div v-else>
    <p>loading job details...</p>
</div>
</template>

<script>

export default {
    props: ['id'],
    data() {
        return {
            recipe: null
        }
    },
    mounted() {
        fetch(`http://127.0.0.1:8000/recipes/${this.id}`, {
            method: 'get',
            headers: {
                'Content-Type': 'application/json',
            }
        })
            .then((res) => res.json())
            .then(data => this.recipe= data)
            .catch(err => console.log(err.messages))
    }
}
</script>

<style scoped>

h1 {
    margin-bottom: 40px;
}

img {
    width: 400px;
    margin-left: 200px;
}
.recipe-info {
    display: flex;
    margin-bottom: 36px;
}

.recipe-info p {
    text-align: left;
    padding-left: 20px;
}
</style>