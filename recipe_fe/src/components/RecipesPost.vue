<template>
    <div class="card">
        <router-link :to="{ name: 'recipesDetails', params: { id: recipe.id} }">
            <img v-if="recipe.photo !== null" :src="recipe.photo" alt="">
            <img v-else src="http://127.0.0.1:8000/media/recipes/default-food-image.jpg" alt=""></router-link>
        <div class="info-recipe">
            <router-link :to="{ name: 'recipesDetails', params: { id: recipe.id} }">
                <h2>{{ recipe.title }}</h2>
            </router-link>
            <div class="info-card">
                <div class="rate">
                    <div>
                        <span><i class="fa fa-star"></i></span>
                        <span class="avg-rate">&nbsp;{{ recipe.avgRate }}</span>
                    </div>
                </div>
                <span class="field">Category:</span>
                <span class="value">
                    <button :value="recipe.category"
                            class="button-category">
                        {{ recipe.category }}
                    </button>
                </span>
            </div>
            <p><span class="field">Time: </span><span class="value">{{ recipe.time_in_minutes }} min</span></p>
            <p><span class="field">author: </span><span class="value">{{ recipe.author }}</span></p>
            <p><span class="field">Published: </span><span
                class="value">{{ recipe.publication_date.split('T')[0] }}</span></p>
        </div>
    </div>
</template>

<script>

export default {
    name: "RecipePost",
    props: {
        recipe: Object,
    },

}
</script>

<style scoped>

button.button-category{
    padding: 2px 10px;
    background: none;
    border: 1px solid darkgray;
    border-radius: 3px;
    color: black;
    font-weight: bold;
}

button.button-category:hover{
    cursor: pointer;
}

.card .info-recipe {
    text-align: left;
    margin-left: 20px;

}

.info-card .avg-rate {
    font-size: 20px;
}

.info-card .fa.fa-star {
    font-size: 22px;
}

.card {
    display: flex;
    border-radius: 4px;
    background: white;
    margin-bottom: 2px;
    width: 1100px;
}
span.field{
    font-style: italic;
    text-transform: lowercase;
    background: darkgrey;
    color: white;
    border-radius: 4px;
    padding: 2px 8px;
    margin-right: 6px;
}
span.value {
     letter-spacing: 1px;
     font-size: 18px;
     font-weight: bold;
}
</style>