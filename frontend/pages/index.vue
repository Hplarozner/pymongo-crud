<template>

  <v-row no-gutters justify="space-between" class="pa-4">
    <v-col cols="4" class="pa-2">
      <v-card density="compact" prepend-avatar="/python.png" class="mx-auto" title="Pymongo Todo App"> 
        <v-divider></v-divider>
          <v-form @submit.prevent="save" ref="form_ref">
            <v-card-text>
              <v-text-field density="compact" label="Firstname" v-model="form.firstname"/>
              <v-text-field density="compact" label="Middlename" v-model="form.middlename"/>
              <v-text-field density="compact" label="lastname" v-model="form.lastname"/>
              <v-text-field density="compact" label="Phone" v-model="form.phone"/>
              <v-text-field density="compact" label="Email" v-model="form.email"/>
            </v-card-text>  

            <v-card-actions>
              <v-btn density="compact" variant="elevated" type="submit">Save</v-btn>
              <v-btn density="compact" variant="elevated" @click="update_user">Update</v-btn>
            </v-card-actions>         
          </v-form>
      </v-card>
    </v-col>

    <v-col cols="8" class="pa-2">
      <v-card title="List of Users" prepend-avatar="/team.png" density="compact" class="mx-auto">
        <v-divider></v-divider>
          <v-virtual-scroll
            :items="list_of_users"
            height="395"
            item-height="48"
          >
            <template v-slot:default="{ item, index }">
              <v-list-item
                :subtitle="`Badge #${index + 1}`"
                :title="`${item.firstname} ${item.lastname}`"
              >
              <template v-slot:prepend>
                <v-avatar class="text-white" size="40">
                  {{ item.initials }}
                </v-avatar>
              </template>

              <template v-slot:append>
                <v-btn density="compact" @click="show_update(item)">Update</v-btn>
              </template>
              </v-list-item>
            </template>
          </v-virtual-scroll>
      </v-card>
    </v-col>
  </v-row>

  <!-- <div>
    <h1>Todos</h1>
    <ul>
      <li v-for="todo in todos" :key="todo._id">
        {{ todo }}
        <button @click="updateTodo(todo._id)">Edit</button>
        <button @click="deleteTodo(todo._id)">Delete</button>
      </li>
    </ul>
    <input type="text" v-model="newTodo.title" placeholder="Enter new todo">
    <button @click="addTodo">Add Todo</button>
  </div> -->
</template>

<script setup lang="ts">
import { onBeforeMount, ref } from 'vue'

onBeforeMount(() => {
  fetch_data()
})

const form = ref({
  firstname  : "",
  middlename : "",
  lastname   : "",
  phone      : "",
  email      : "",
})

const form_ref = ref();
const list_of_users = ref([])

async function fetch_data(){
  const response = await fetch('http://localhost:5000/todos' , {
    method: "GET",
  })

  const data = await response.json();
  list_of_users.value = data.map((v: any) => ({
    initials: `${v.firstname[0]} ${v.lastname[0]}`,
    ...v
  }))
}

async function save(){
  const response = await fetch("http://localhost:5000/todos", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(form.value),  
  });
  form_ref.value.reset()
  fetch_data()
}

function show_update(item: any){
  form.value = item
}

async function update_user(){
  console.log(form.value._id)
  const response = await fetch(`http://localhost:5000/todos/${form.value?._id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(form.value),  
  })

  console.log(response)

  fetch_data()
  //       try {
//         const response = await fetch(`http://localhost:5000/todos/${id}`, {
//           method: "PUT",
//           headers: {
//             "Content-Type": "application/json",
//           },
//           body: JSON.stringify({   
//  title: prompt("Enter new title") }),
//         });
//         const data = await response.json();
//         console.log(data);
//         const index = this.todos.findIndex((todo) => todo._id === id);
//         this.todos[index].title = prompt("Enter new title");
//       } catch (error) {
//         console.error(error);
//       }

}
// export default {
//   data() {
//     return {
//       todos: [],
//       newTodo: {
//         title: "",
//       },
//     };
//   },
//   async mounted() {
//     try {
//       const response = await fetch("http://localhost:5000/todos")
//       const data = await response.json();
//       this.todos = data;
//     } catch (error) {
//       console.error(error);
//     }
//   },
//   methods: {
//     async addTodo() {
//       try {
//         const response = await fetch("http://localhost:5000/todos", {
//           method: "POST",
//           headers: {
//             "Content-Type": "application/json",
//           },
//           body: JSON.stringify(this.newTodo),   

//         });
//         const data = await response.json();
//         console.log(data);
//         this.todos.push(this.newTodo);
//         this.newTodo.title = "";
//       } catch (error) {
//         console.error(error);
//       }
//     },
//     async updateTodo(id) {
//       try {
//         const response = await fetch(`http://localhost:5000/todos/${id}`, {
//           method: "PUT",
//           headers: {
//             "Content-Type": "application/json",
//           },
//           body: JSON.stringify({   
//  title: prompt("Enter new title") }),
//         });
//         const data = await response.json();
//         console.log(data);
//         const index = this.todos.findIndex((todo) => todo._id === id);
//         this.todos[index].title = prompt("Enter new title");
//       } catch (error) {
//         console.error(error);
//       }
//     },
//     async deleteTodo(id) {
//       try {
//         const response = await fetch(`http://localhost:5000/todos/${id}`, {
//           method: "DELETE",
//         });
//         const data = await response.json();
//         console.log(data);
//         this.todos = this.todos.filter((todo) => todo._id !== id);
//       } catch (error) {
//         console.error(error);
//       }
//     },
//   },
// };
</script>