<template>
    <NavBar/>
    <div>
        <img class="index-img" src="http://127.0.0.1:8000/media/background.jpg"
             alt="main-picture">
    </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import axios from "axios";

export default {
    name: 'HomeView',
    components: {NavBar},

    mounted() {
        this.getCurrentUser()
    },
    methods: {
        getCurrentUser(){
            axios
                .get('/auth/login/')
                .then(response => {
                    console.log(response.data)

                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>

<style>
body, html {
  height: 100%;
}

.index-img {
    height: 100%;

    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
</style>
