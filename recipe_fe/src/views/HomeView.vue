<template>
    <NavBar/>
    <div class="banner">
        <div class="content">

            <h1>Welcome to Recipes Blog</h1>
            <div class="item-links">


                <div class="item" v-if="is_logged">
                    <a href="/recipes/create">
                        <h3>Share your favorite recipes </h3>
                        <p>Create post</p>
                    </a>
                </div>

                <div class="item">
                    <a href="/recipes">
                        <h3>View all recipes</h3>
                        <p>Gallery</p>
                    </a>
                </div>

                <div class="item">
                    <a href="/recipes/dessert">
                        <h3>Life is short, eat dessert first. </h3>
                        <p>Desserts</p>
                    </a>
                </div>

            </div>
        </div>
    </div>

    <div>
        <Footer/>
    </div>

</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";
import Footer from "@/components/Footer";

export default {
    name: 'HomeView',
    components: {Footer, NavBar},
    data(){
        return {
            desserts: [],
            is_logged: (localStorage.getItem('token') !== null),
        }
    },
    mounted() {
        this.getCurrentUser()
    },
    methods: {
        getCurrentUser(){
            axios
                .get('/auth/login/')
                .then(response => {
                    console.log(response.data)
                    document.title = 'Home | Recipes Blog'
                })
                .catch(error => {
                    console.log(error)
                })
        },

    }
}
</script>

<style scoped>

* {
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}

div.banner{
    width: 100%;
    height: 100vh;
    background-image: linear-gradient(
        rgba(0,0,0,0.75),
        rgba(0,0,0,0.75)),
        url("http://127.0.0.1:8000/media/index/background.jpg");
    background-size: cover;
    background-position: center;
}

.content  {

    width: 100%;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    text-align: center;
    color: white;
}

.item {
    background: linear-gradient(
        rgba(238, 232, 232, 0.75),
        rgba(213, 208, 208, 0.75));
    height: 100px;
    width: 500px;
    margin-top: 100px;
    padding-top: 20px;
    border-radius: 20px;
}

.item-links {
    display: flex;
    justify-content: space-evenly;
}

.item h3 {
    text-transform: uppercase;
}

.item p{
    text-decoration: underline;
    font-size: 20px;
    text-transform: uppercase;
    color: darkslategray;
}

.content h1 {
    margin: 20px auto;
    font-weight: bold;
    font-size: 70px;
    text-transform: uppercase;
    letter-spacing: 2px;
    line-height: 25px;
    color: white;
}

</style>
