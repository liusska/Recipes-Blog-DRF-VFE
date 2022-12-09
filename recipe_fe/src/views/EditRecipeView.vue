<template>
    <NavBar/>
    <form @submit.prevent="editPost" enctype="multipart/form-data">
        <label class="label">Title</label>
        <input  class="input is-primary" type="text" v-model="title">

        <label class="label">Ingredients</label>
        <input class="input is-primary"  type="text" v-model="ingredients">

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
                <input type="file" ref="file" @change="selectFile" accept="image/*" :src=photo>
            </label>
        </div>

        <label class="label">Video</label>
        <input class="input is-primary"  type="url" v-model="video">

        <label class="label">Time</label>
        <input class="input is-primary"  type="text" v-model="time_in_minutes">

        <label class="label">Description</label>
        <textarea class="textarea is-primary"  cols="76" rows="10" v-model="description"></textarea>

        <div class="field is-grouped">
            <div class="control">
                <button class="button is-primary">Edit post</button>
            </div>

            <div class="control">
                <button class="button is-link is-light">Cancel</button>
            </div>
        </div>
    </form>

    <div v-if="error">
        <strong>{{ error }}</strong>
    </div>
</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";

export default {
    name: 'EditRecipeView',
    components: {NavBar},
    props: ['id'],
    data() {
        return {
            old_photo: null,
            photo: null,
            title: '',
            ingredients: '',
            category: '',
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
            ],
            error: '',
        }
    },
    mounted() {
        console.log("recipe id: " + this.id)
        axios.get(`/recipes/${this.id}`)
            .then(response => {
                this.title = response.data.title
                this.ingredients = response.data.ingredients
                this.category = response.data.category
                this.old_photo = response.data.photo
                this.photo = response.data.photo
                this.video = response.data.video
                this.time_in_minutes = response.data.time_in_minutes
                this.description = response.data.description
            })
            .catch(err => console.log(err.messages))

    },
    methods: {
        editPost() {
            console.log('photo', this.photo)

            const dataForm = {
                title: this.title,
                ingredients: this.ingredients,
                category: this.category,
                photo: this.photo,
                video: this.video,
                time_in_minutes: this.time_in_minutes,
                description: this.description,
            }

            if (typeof this.photo === 'string') {
                dataForm.photo = this.urlToObj(this.photo)
            }

            axios.put(`/recipes/${this.id}/`, dataForm, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                }
            })
                .then(resp => {
                    console.log(resp)
                    this.$router.push(`/recipes/${this.id}`)
                })
                .catch(error => {
                    this.error = error
                    console.log(error)
                })
        },
        selectFile() {
            this.photo = this.$refs.file.files.item(0)
        },
        urlToObj(url) {
            let dir = {}
            let paths = url.split('/')
            paths.reduce(function (dir, path) {
                return dir[path] = {}
            }, dir)
            return dir
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

/*label {*/
/*    color: #aaa;*/
/*    display: inline-block;*/
/*    margin: 25px 0 15px;*/
/*    font-size: 0.8em;*/
/*    text-transform: uppercase;*/
/*    letter-spacing: 1px;*/
/*    font-weight: bold;*/
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

/*button {*/
/*    background: #0b6dff;*/
/*    border: 0;*/
/*    padding: 10px 20px;*/
/*    margin-top: 20px;*/
/*    color: white;*/
/*    border-radius: 20px;*/
/*}*/

/*.submit {*/
/*    text-align: center;*/
/*}*/
</style>