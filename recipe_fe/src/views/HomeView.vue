<template>
    <NavBar/>
    <div>
        <img class="index-img" src="https://iamafoodblog.b-cdn.net/wp-content/uploads/2020/11/korean-bbq-8064w.jpg"
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
.index-img {
    height: 600px;
    margin-top: 36px;
    padding-left: 0;
}
</style>
