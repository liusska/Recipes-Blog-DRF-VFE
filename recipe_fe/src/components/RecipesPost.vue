<template>
    <div class="card">
        <div class="card-image">
            <figure class="image is-5by4">
                <router-link :to="{ name: 'recipesDetails', params: { id: recipe.id} }">
                    <img v-if="recipe.photo !== null" :src="recipe.photo" alt="recipe-image">
                    <img v-else src="http://127.0.0.1:8000/media/recipes/default-food-image.jpg" alt="default-recipe-img">
                </router-link>
            </figure>
        </div>
        <router-link :to="{ name: 'recipesDetails', params: { id: recipe.id} }">
        <div class="card-content">
            <div class="media">
                <div class="media-content">
                    <div class="title is-4">
                        <div>
                            <span><i class="fa fa-star"></i></span>
                            <span class="subtitle is-5">&nbsp;{{ recipe.avgRate }}</span>
                        </div>
                        <p>{{ recipe.title }}</p>

                        <span class="value">
                            <button class="button is-link is-inverted" :value="recipe.category">{{ recipe.category }}</button>
                        </span>
                    </div>
                    <p class="subtitle is-5">author: {{ recipe.author }}</p>
                    <p class="subtitle is-7">time: {{ recipe.time_in_minutes }} min | {{ recipe.publication_date.split('T')[0] }}</p>
                </div>
            </div>
        </div>
        </router-link>

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

.fa.fa-star {
    font-size: 22px;
    color: yellow;
}

.card {
    margin-top: 58px;
    width: 500px;
}

</style>