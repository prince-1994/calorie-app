<template>
  <div>
    <form @submit.prevent="saveToken">
      <b-field label="Token">
        <b-input v-model="token"></b-input>
      </b-field>
      <b-button native-type="submit" type="is-primary">Save Token</b-button>
    </form>
  </div>
</template>

<script>
export default {
  auth: false,

  data() {
    return {
      token: '',
    }
  },

  mounted() {
    this.token = this.$store.state.token
  },

  methods: {
    saveToken() {
      this.$store.dispatch('saveToken', this.token).then(() => {
        if (this.$store.state.authenticated) {
          this.$router.push('/')
        }
      })
    },
  },
}
</script>

<style></style>
