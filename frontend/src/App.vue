<template>
  <div id="app">
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
  </div>
</template>
<!--  啟動 npm run dev  -->
<script>
import { ref, onMounted } from 'vue'

export default {
  name: 'App',
  setup() {
    const title = ref('Welcome to YurVue.js + Flask App')
    const message = ref('Loading...')

    onMounted(async () => {
      try {
        console.log('Fetching data from server...')
        const response = await fetch('http://localhost:5001/api/hello')
        console.log('Response status:', response.status)
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const data = await response.json()
        console.log('Received data:', data)
        message.value = data.message
      } catch (error) {
        console.error('Error:', error)
        message.value = `Failed to fetch message from server: ${error.message}`
      }
    })

    return {
      title,
      message
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>