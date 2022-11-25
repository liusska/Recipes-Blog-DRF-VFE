<template>
    <NavBar />

    <div v-if="recipes.length" class="gallery">
        <h1><span class="username-field">{{user}}</span> Recipe Posts</h1>
        <div v-for="recipe in recipes" :key="recipe.id">
            <div class="card">
                <img v-if="recipe.photo !==''" :src="recipe.photo" alt="">
                <img v-else src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPUAAADOCAMAAADR0rQ5AAAAP1BMVEX49/Ho0qvn0aj5+fX39e328+nq1rPp1bDq17Xs27zo06zs3L749vD28ufn0Kbx59Pv4srz69vw5M307uDu38UqK0Z9AAAI/ElEQVR4nO2daZeqOBCGNQFZRBTh///WSSBLJVURdXrG0lPvhz73tsvxIbUn2IeDSCQSiUQikUgkEolEIpFIJBKJRCKRSCQSiUQikUgkEolEIpFIJPrvpA86yvzv12Uoh3qe7rfl3Fmdl9t9muvB0v+o9KGe713bq03H49H9q2+7+1z/4qLrYb6vwEdKK/p9Hn4MfL61BWCI3t7mT3/QP5OurvvIAfxa/cKC6/rWPIfswJtb/e3chrl/hXnl7r+cu7q/zLxx36tPf/T3NZ3eYV65T9OnP/x70vX5XeaV+/yNZq6nt4wbYPfTt2HrYfl3zCv38mVZ7NLu1iTHpjnuPEm1l0+DvCA976VoU41c6vqyZxCqmb9nta8763xU963X0LddP7h+GuZZXXet++pXsO53L9CXYN93oZfw3Oq0R23t4gu0C31s6vDkqtml/gZsvWveZqljhKqfoAYOwVR62k/TCjTR+369voJ5vTI/wXACncVz1Mcj62nDMwarzmDh6uegYSjgp+6JMjRJRRficUVM11T3MaY9PVFzHFO3PlzyV6h+meZpQbWqujF1bT0/1XAoWFvn1La/tJsEuEtVTGvTAVYcffoDKHHR/ELFHIUy4Gn4ANOuoH2rpW6NA9cnk3RmE+HmKbLDEJ5TgwyFEj9PG4eByZjjTalaL6qvdKcMaBsea8Fr0vSeViO43uHYdsL4PdZ25S11U+uzodaBWnUALaGGNduqrA/lGMfTVbPUZpkNdWWoG7vg/qFziRo5bl6kK34TxBZ+vr7egOOPEJPTFQVWTDDl5W2LnvFhpR8wAXY/PNyNplZn4l2zqofbYutkqU2cNpgnB3yzP+40NWhLiVIbVQAtqzCet1rtsFE7YBPSriQ1uBh0qOpSal7Nl85MsTsYaoN+s+jXB9Qhxxd4pjyMc6LOmggTpy31wVP3dfz4KXVw94be2Kryyo5RztbZ1MhSn43Nmt+bAsWsdRWLMJo6yWfwnbN6XN0ZLXY28zPZyfCcHfVknbtA7aGKDpsXaCc+1PkExZAZnrMN0ca5J2PhOvhAkq/jUpYsF7WibKYquYHbwYGl1hv1bKnDqCil9lHwVNqvRvUZGxPPkrWnNnhXTx1nSxm1+205NufvzSZlo5Gf8dKE+ljHcX8atzrql4ny8ULPZIKGp8FqtrZ7W6nXtFaDgJcsq1vJcu+s8w1ALoUKHpeNF2vhxgOvY+epg6XCImzw1EVvRW/OZbiA3No0mnatr4eNuu7X/wfHBA2lHzq9QM3FsQc8BLeUowlpU6QO/gnDtff2BxaOqBse8zM80+6rhLqx1GTt6fPSC37NpCgltrYMmG5HE8hX6qpRF7BmMAj7fPZCDOcSzvAu5mlIqE92BB57SrBWIeeV83WXvzmPbXxix6O1IW6crYXbCUlrYnq8NuSWZnHYjTe4eQRxwvM6TB39AFpo2Nwr1h413vLKR6kfUT5R2EZgekWdR+Ow7p+BGlho7EkK+zlE0OAxWSDS9bKimuWL1KDBBrn5Qvaf8M2Js1ksErZGB2osgj5F6s5Sk61m7CMLQ98BXVImLbYm442erCFXdxu65vsAqUGWAjNQOguj9tqoYUptVzP/aBGwo6jpmpTcEedKTdQcICzFQhzGKjJ3kQezeFBj1yMGniAsxUchNbWvQR/j4hHNMDWVh2LMi7k53dzDb030NWyo8REcYs8KrmoMXHAtsWfT51yY5GsipaIOATooKElTC87Hn/Q5Fya1GXlwNL1pIxnmg0uSvjQNB7pweI3HlJQ+RJkQpOYQT8NmF0y18EVV4QYhJp0maYgKjkxSH4gmmjuuAtOlEnR6Xu1zos+CRgJiF8w/ggagcZRYvHGEyWgYlykbgfc/VFV2ReqQtR8cuGZRpOB9x/DxNhvHaNEKyNZ8FdF1uOtSHjb9vyqsy+gcEPVkweWJ6+VOHuJhQqBmMUA6lPKq/3wX5PbhTCVV4KyX6tHheh7BrFQ4+lhNXBOfzAd8r4u7VA/cmsc4vOjYW+lILVu/oQ1EnN6GKlS95x7n4tZFe9wiE7FsrpSm+sjNQB5Q86hRrAp3b6yxmipY3YJRN3O5h4o3MTPJ1lZEVLJaYzXVODmPJ9zaURfekJOBF028TO0qcSIpO+MvUvMxcCMyipepXc59nZpNBLeiu82NmvLrbcU02sMKFl7wax5dZhB5X9ZWeVLU2zSFYntMfeQTy6zIVFPMXG74TU5hHmUuHmMUIOp2tJWainTFviRUKYU7w1hs2AMRBM5YiYrUzb5Jl98CHRkn2C01VamU63DfTlJl24M6nFGF4oUXzgVcbPu+1KBGB9sonSwAmAXwTajScstGGIHbtqXY3FRsHjE1y5v3kAO7rIyr7TAYIIy/3wIWMVVgeqNmHtBGl5/wrr4vK4l9Whfei1GCn/JV3YIPrjjClg+R7k70Wz04S/1p6fR0fDkr+1hMdKh+foqKVZ72bZUGZT8KRZE6zM3wno63Y3S/B+uv0QDr6jc2caQOk2Ei0LnslBVn4HtlWCq2iCH8oEgddgHwWZsQ6BID4Xg3bqIqTABDfspHw2Aegqn93BdeqnTXj6N07XflwrKhG1bi7h6KWb0P7yBh21v/PoHyivTFfbfZ6AHyhB0rS5zUwgZwDO+qubCHtthutcMOB4rH4al4C8w/FFxenb4B2hr56ttxNyvfpQ4TP2InNxC6sKha/ua9SVf2I8e4e32eeskeUt03fWHjosDefH478QPqaPxr48o9T2cyVVo8BZzfp/yAeoKXSh1ZV2SU5nhWMCs8H1HHbdp5/K7v5UTKEjYwY3Q7YuSsx9uXf3V8+yw1/EZDLrvz7yorwcD8K6/NWA6J3lS2pCDOsb3N+A+kS6fsUKf5U9S3McEO9QuaKrA4DvxXqqZzD76LMEwV8kQ+/tJa25tA6msXwENjlTTRqu+u/DY3/q10PS3uz9m4rOzGbNsftblN39JmvCht/5LPdelOLhXrZTz2TdstV/tXfH6T2QvgXeZLXQ0/zisSiUQikUgkEolEIpFIJBKJRCKRSCQSiUQikUgkEolEIpFIJBKJRCLR3+of02dYVoLpV6wAAAAASUVORK5CYII="  alt="">

                <div class="info-recipe">
                    <router-link :to="{ name: 'recipesDetails', params: { id: recipe.id} }">
                        <h2>{{ recipe.title }}</h2>
                    </router-link>

                    <p><span class="field">Category: </span><span class="value">{{ recipe.category }}</span></p>
                    <p><span class="field">Ingredients: </span><span class="value">{{ recipe.ingredients }}</span></p>
                    <p><span class="field">Time: </span><span class="value">{{ recipe.time_in_minutes}} min</span></p>
                    <p><span class="field">author: </span><span class="value">{{ recipe.author }}</span></p>
                    <p><span class="field">Published: </span>
                        <span class="value">
                            {{recipe.publication_date.split('T')[0]}}
                            {{ (recipe.publication_date.split('T')[1]).split('.')[0]}}
                        </span></p>
                </div>
            </div>
        </div>
    </div>

    <h1 v-else>*** No content yet ***</h1>

</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar";

export default {
    name: "ProfileView",
    components: { NavBar },
    data() {
        return {
            recipes: [],
            user: null,
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
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log(error)
                })
            this.getUserRecipes()
        },
        getUserRecipes(){
            axios.get(`/recipes/user/`)
            .then(response => {
                for (let item in response.data){
                    response.data[item].photo = `http://127.0.0.1:8000${response.data[item].photo}`
                    this.recipes.push(response.data[item])
                }
            })
            .catch(err => console.log(err.messages))
        },
    }


}
</script>

<style>

body {
    background: whitesmoke;
}
.gallery {
    margin: 40px auto;
    width: 900px;

}
img {
    padding-left: 0;
}
.card {
    display: flex;
    border-radius: 4px;
    background: white;
    margin-bottom: 2px;

}
.card img{
    height: 300px;
    border-radius: 0 28px 28px 0;
    border: 5px white solid;
}
.card .info-recipe {
    text-align: left;
    margin-left: 20px;

}
.info-recipe a{
    text-decoration: none;
    color: #2c3e50;
    font-size: 26px;
}
span.username-field {
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #0b6dff;
}

</style>