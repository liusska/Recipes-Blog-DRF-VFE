<template>
  <NavBar/>

<div class="container">
    <a href="/recipes">
        <div class="welcome">
            <img class="index-img" src="http://127.0.0.1:8000/media/index/welcome.jpg" alt="welcome-img">
            <p>View all recipes</p>
        </div>
    </a>
    <div class="menu">
        <div class="create-item">
        <a href="/recipes/create">
            <img class="index-img" src="http://127.0.0.1:8000/media/index/create.jpg" alt="welcome-img">
            <h4>Share with as </h4>
            <p>your favorite recipe </p>
        </a>
    </div>

    <router-link to="/recipes/dessert">
    <div class="desserts">
        <img class="index-img" src="http://127.0.0.1:8000/media/index/desserts.jpg" alt="welcome-img">
        <h4>Life is short,</h4>
        <p>eat dessert first.</p>
    </div></router-link>
</div>


  <div>
      <Footer/>
  </div>
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
            desserts: []
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

/*.container {*/
/*    margin: 0 auto;*/
/*    width: 70vw;*/
/*    height: 80vh;*/
/*}*/

/*.container > div {*/
/*    text-align: center;*/
/*    padding: 20px 0;*/
/*    font-size: 30px;*/
/*}*/

/*.menu {*/
/*    display: flex;*/
/*    justify-content: space-between;*/
/*}*/

/*body {*/
/*    box-sizing: border-box;*/
/*    padding: 0;*/
/*    margin: 0;*/
/*}*/

/*.desserts h4, .desserts p, .create-item p, .create-item h4, .welcome p{*/
/*    position: absolute;*/
/*    border: 4px solid white;*/
/*    background: white;*/
/*    font-size: 40px;*/
/*    color: #555555;*/
/*    font-style: italic;*/
/*    text-transform: uppercase;*/
/*    font-weight: bold;*/
/*}*/

/*.index-img{*/
/*    image-resolution: normal;*/
/*    width: 1200px;*/
/*}*/

/*.welcome {*/
/*    grid-area: header;*/
/*    position: relative;*/
/*    margin-top: 30px;*/
/*    z-index: -1;*/
/*}*/

/*.welcome p {*/
/*    right: 400px;*/
/*    bottom: 60px;*/
/*}*/

/*.create-item h4{*/
/*    left: 400px;*/
/*    bottom: -160px;*/
/*}*/

/*.create-item p {*/
/*    left: 320px;*/
/*    bottom: -180px;*/
/*}*/

/*.create-item img {*/
/*    width: 590px;*/
/*    height: 400px;*/
/*}*/

/*.desserts:hover {*/
/*    cursor: pointer;*/
/*}*/
/*.desserts img {*/
/*    grid-area: right;*/
/*    width: 590px;*/
/*    height: 400px;*/
/*}*/

/*.desserts h4 {*/
/*    right: 130px;*/
/*    bottom: -60px;*/
/*}*/

/*.desserts p {*/
/*    right: 90px;*/
/*    bottom: -170px;*/
/*}*/

/*a:hover {*/
/*    cursor: pointer;*/
/*}*/

</style>
