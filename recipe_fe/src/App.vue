<template>
    <nav>
        <div>
            <router-link to="/">Home</router-link>
            <router-link to="/recipes">Recipes</router-link>
            <router-link to="/create">Create</router-link>
        </div>
        <div>
            <router-link to="/register" v-if="!is_logged">Register</router-link>
            <router-link to="/login" v-if="!is_logged">Login</router-link>

            <router-link to="/profile">Profile</router-link>
            <button @click="logout()" v-if="is_logged">Logout</button>

        </div>

    </nav>
    <router-view/>
</template>

<script>
import axios from "axios";
export default {
    data(){
        return{
            is_logged: (localStorage.getItem('token') !== null)
        }
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            console.log('logout')
            this.$router.push('/')
        },
    },
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}

nav {
    padding: 16px;
    display: flex;
    justify-content: space-between;
}


nav a {
    font-weight: bold;
    text-decoration: none;
    letter-spacing: 0.5px;
    color: #2c3e50;
    font-size: 26px;
    margin: 10px;
}

nav a.router-link-exact-active {
    color: slategrey;
}
button:hover {
    cursor: pointer;
}

</style>
