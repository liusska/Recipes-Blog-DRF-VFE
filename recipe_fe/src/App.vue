<template>
<!--    <NavBar/>-->
    <router-view/>
</template>

<script>
import NavBar from "@/components/NavBar";

export default {
    components: { NavBar }
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    /*background-image: linear-gradient(*/
    /*    rgba(0,0,0,0.75),*/
    /*    rgba(0,0,0,0.75)),*/
    /*    url("http://127.0.0.1:8000/media/index/background.jpg");*/
    /*width: 100%;*/
    /*background-size: cover;*/
    /*background-position: center;*/
    /*background-repeat: round;*/
}

</style>
