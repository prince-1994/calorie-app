export const state = () => ({
  messages: [],
  token: '',
  messageCounter: 0,
  userProfile: null,
  authenticated: false,
})

export const mutations = {
  addMessage(state, message) {
    message.id = state.messageCounter
    state.messages.push(message)
    state.messageCounter++
  },

  removeMessage(state, message) {
    state.messages.splice(
      state.messages.findIndex((msg) => msg.id === message.id),
      1
    )
  },

  saveToken(state, token) {
    state.token = token
  },

  initialize(state) {
    state.token = localStorage.getItem('access_token') || ''
  },

  setUserProfile(state, userProfile) {
    state.userProfile = userProfile
  },

  setAuthenticated(state, authenticated) {
    state.authenticated = authenticated
  },
}

export const actions = {
  addTemporaryMessage(context, message) {
    context.commit('addMessage', message)
    setTimeout(context.commit, 5000, 'removeMessage', message)
  },

  addMessage(context, message) {
    context.commit('addMessage', message)
  },

  saveToken(context, token) {
    context.commit('saveToken', token)
    localStorage.setItem('access_token', token)
    this.$axios.setToken(token, 'Token')
    return context.dispatch('fetchUserProfile')
  },

  fetchUserProfile(context) {
    return this.$axios
      .get('/api/userprofiles/profiles/')
      .then((result) => {
        context.commit('setUserProfile', result.data)
        context.commit('setAuthenticated', true)
      })
      .catch(() => {
        context.dispatch('addTemporaryMessage', {
          message: 'Authentication has failed. Please set your user token.',
          type: 'error',
        })
        context.commit('setAuthenticated', false)
      })
  },
}
