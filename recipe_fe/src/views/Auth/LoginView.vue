<template>
    <NavBar/>

    <form @submit.prevent="LoginFunc">
        <label>Email</label>
        <input type="email" required v-model="email">

        <label>Password</label>
        <input type="password" required v-model="password">

        <div class="submit">
            <button>Login</button>
        </div>
        Or <router-link to="/register">click here</router-link> to register

    </form>
</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";

export default {
    components: {NavBar},
    data() {
        return {
            email: '',
            password: ''
        }
    },
    methods: {
        async LoginFunc() {
            const formData = {
                email: this.email,
                password: this.password,
            }
            const response = await axios.post('/auth/login/', formData);
            localStorage.setItem('token', response.data.token)
            localStorage.getItem('token')
            axios.defaults.headers.common['Authorization'] = localStorage.getItem('token')

            this.$router.push('/')

        },
    }
}
</script>

<style>
    form {
        max-width: 420px;
        margin: 30px auto;
        background: white;
        text-align: left;
        padding: 40px;
        border-radius: 10px;
    }
    label {
        color: #aaa;
        display: inline-block;
        margin: 25px 0 15px;
        font-size: 0.6em;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: bold;
    }
    input, select {
        display: block;
        padding: 10px 6px;
        width: 100%;
        box-sizing: border-box;
        border: none;
        border-bottom: 1px solid #ddd;
        color: #555;
    }
    input[type="checkbox"] {
        display: inline-block;
        width: 16px;
        margin: 0 10px 0 0;
        position: relative;
        top: 2px
    }
    button {
        background: #0b6dff;
        border: 0;
        padding: 10px 20px;
        margin-top: 20px;
        color: white;
        border-radius: 20px;
    }
    .submit {
        text-align: center;
    }
</style>