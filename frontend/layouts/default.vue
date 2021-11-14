<template>
  <div class="columns is-centered">
    <div class="column is-10">
      <b-navbar :mobile-burger="false">
        <template #brand>
          <b-navbar-item tag="router-link" :to="{ path: '/?' }">
            <strong class="is-size-3">Simple Calorie App</strong>
          </b-navbar-item>
        </template>
        <template #start> </template>
        <template #end> </template>
      </b-navbar>
      <div class="">
        <b-message
          v-for="message in $store.state.messages"
          :key="message.id"
          :title="message.type === 'error' ? 'Error' : 'Success'"
          :type="message.type === 'error' ? 'is-danger' : 'is-success'"
        >
          {{ message.message }}
        </b-message>
        <Nuxt />
      </div>
    </div>
  </div>
</template>
