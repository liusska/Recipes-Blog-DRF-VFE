<template>
    <div class="home">
        <h1 v-if="user">Welcome to Home page {{user}}</h1>
        <h1 v-else>Welcome to Home page, Anonymous</h1>
    </div>
    <div>
        <img src="https://thumbor.forbes.com/thumbor/fit-in/900x510/https://www.forbes.com/home-improvement/wp-content/uploads/2022/07/featured-image-kitchen-layouts.jpg" alt="">
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: 'HomeView',
    data(){
        return {
            user: null
        }
    },
    async created(){
        const response = await axios.get('/auth/login/')
        console.log(response)
        this.user = response.data.user

    }
}
</script>
