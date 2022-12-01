<template>
     <nav>
        <div>
            <router-link class="home-button" to="/"><i class="fa fa-home"></i>Home</router-link>
            <router-link to="/recipes">Recipes</router-link>
            <router-link to="/recipes/create" v-if="is_logged">Create</router-link>
        </div>

        <div>
            <router-link to="/register" v-if="!is_logged">Register</router-link>
            <router-link to="/login" v-if="!is_logged">Login</router-link>

            <router-link to="/profile" v-if="is_logged"><i class="fa fa-user">Profile</i></router-link>
            <button class="logout-button" @click="logout()" v-if="is_logged">Logout</button>

        </div>
    </nav>
</template>

<script>
import axios from "axios";

export default {
    data(){
        return{
            is_logged: (localStorage.getItem('token') !== null),
        }
    },
    mounted() {

    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            this.$router.push('/login')
        },
    },
}
</script>

<style scoped>
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
button {
    margin-top: 0;
    background: #2c3e50;
}
button:hover {
    cursor: pointer;
}
.home-button{
    text-transform: uppercase;
    border: 3px solid gray;
    border-radius: 4px;
    padding: 8px 16px;

}
.logout-button{
    font-size: 18px;
    font-weight: bold;
    text-transform: uppercase;
    background: grey;
    margin: 10px 30px;
    padding: 10px 18px;
}

</style>