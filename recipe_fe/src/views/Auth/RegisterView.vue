<template>
    <NavBar/>
    <form @submit.prevent="registerFunc">
        <label>Email</label>
        <input type="email" v-model="email">

        <label>username</label>
        <input type="text" v-model="username">

        <label>Password</label>
        <input type="password" v-model="password">

        <label>Repeat Password</label>
        <input type="password" v-model="rePassword">

         <div class="error" v-if="errors.length">
             <ul v-for="error in errors" :key="error">
                 <li>{{ error }}</li>
             </ul>
         </div>
        <div class="submit">
            <button>Create an account</button>
        </div>
        Or <router-link to="/login">click here</router-link> to login
    </form>
    <div class="footer">
        <Footer/>
    </div>
</template>

<script>
import axios from 'axios'
import NavBar from "@/components/NavBar";
import Footer from "@/components/Footer";

export default {
    name: 'Register',
    components: {NavBar, Footer},
    data() {
        return {
            email: '',
            username: '',
            password: '',
            rePassword:'',
            errors: [],
        }
    },
    mounted() {
        document.title = 'Register | Recipes Blog'
    },
    methods: {
        registerFunc() {
            this.errors = []
            if (this.username === ''){
                this.errors.push('The username is missing')
            }
            if (this.email === ''){
                this.errors.push('The email is missing')
            }
            if (this.password === ''){
                this.errors.push('The password is too short')
            }
            if (this.password !== this.rePassword) {
                this.errors.push('The password doesn\'t match')
            }
            if (!this.errors.length){
                const formData = {
                    email: this.email,
                    username: this.username,
                    password: this.password,
                }

                axios
                    .post('/auth/register/', formData)
                    .then(response => {
                        console.log(response)
                    })
                    .catch(error => {
                        if (error.response){
                            for (const property in error.response.data){
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            console.log(JSON.stringify(error))
                        }
                    })
                    this.$router.push('/login')
            }

        }
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
    .error {
        color: red;
        margin-top: 10px;
        font-size: 1.2em;
        font-weight: bold;
    }
</style>