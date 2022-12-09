<template>
    <NavBar/>
    <form @submit.prevent="createPost" enctype="multipart/form-data">
        <label class="label">Title</label>
        <input class="input is-primary" type="text" v-model="title">

        <label class="label">Ingredients</label>
        <input class="input is-primary" type="text" v-model="ingredients"
               placeholder="enter ingredients here separate by comma...">

        <div class="field">
            <label class="label">Category:</label>
            <div class="control">
                <div class="select">
                    <select v-model="category">
                        <option v-for="option in options" :value="option.value">
                            {{ option.text }}
                        </option>
                    </select>
                </div>
            </div>
        </div>

        <div class="file is-dark">
            <label class="file-label">
                <input class="file-input" type="file" ref="file" @change="selectFile" accept="image/*"/>
                <span class="file-cta">
                    <span class="file-icon">
                        <i class="fas fa-upload"></i>
                    </span>
                    <span class="file-label">
                        Choose a file…
                    </span>
                </span>
            </label>
        </div>


        <label class="label">Video</label>
        <input class="input is-primary" type="url" v-model="video">

        <label class="label">Time</label>
        <input class="input is-primary" type="text" v-model="time_in_minutes">

        <label class="label">Description</label>
        <textarea class="textarea is-primary" placeholder="Describe steps" v-model="description"></textarea>

        <div class="field is-grouped">
            <div class="control">
                <button class="button is-link">Create post</button>
            </div>

            <div class="control">
                <button class="button is-link is-light">Cancel</button>
            </div>
        </div>

    </form>
    <div>
        <Footer/>
    </div>
</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";
import Footer from "@/components/Footer";


export default {
    name: 'CreateView',
    components: {NavBar, Footer},
    data() {
        return {
            title: '',
            ingredients: '',
            category: '',
            photo: null,
            photo_obj: null,
            video: null,
            time_in_minutes: '',
            description: '',

            options: [
                {text: 'Others', value: 'Others'},
                {text: 'Dessert', value: 'Dessert'},
                {text: 'Snack', value: 'Snack'},
                {text: 'Salad', value: 'Salad'},
                {text: 'Baked', value: 'Baked'},
                {text: 'Main', value: 'Main'},
                {text: 'Pizza', value: 'Pizza'},
            ]
        }
    },
    mounted() {
        document.title = 'Create | Recipes Blog'

    },
    methods: {
        async createPost() {
            console.log(this.photo)
            const dataForm = {
                title: this.title,
                ingredients: this.ingredients,
                category: this.category,
                photo: this.photo,
                photo_obj: this.photo,
                video: this.video,
                time_in_minutes: this.time_in_minutes,
                description: this.description,
            }
            await axios.post('/recipes/', dataForm, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(resp => console.log(resp))
                .catch(error => console.log(error))

            this.$router.push(`/recipes`)
        },

        selectFile() {
            this.photo = this.$refs.file.files.item(0)
        }

    }
}
</script>

<style scoped>
form {
    max-width: 600px;
    margin: 30px auto;
    background: white;
    text-align: left;
    padding: 40px;
    border-radius: 10px;
}

.control {
    margin-top: 20px;
}

.label {
    /*color: #aaa;*/
    /*display: inline-block;*/
    margin: 25px 0 15px;
    /*font-size: 0.8em;*/
    /*text-transform: uppercase;*/
    /*letter-spacing: 1px;*/
    /*font-weight: bold;*/
}

/*::placeholder {*/
/*    color: #555555;*/
/*    font-style: italic;*/
/*}*/

/*input, select {*/
/*    display: block;*/
/*    padding: 10px 6px;*/
/*    width: 100%;*/
/*    box-sizing: border-box;*/
/*    border: none;*/
/*    border-bottom: 1px solid #ddd;*/
/*    color: #555;*/
/*}*/

/*textarea {*/
/*    border-color: snow;*/
/*}*/


/*.submit {*/
/*    text-align: center;*/
/*}*/

</style>