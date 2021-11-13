export default ($axios) => (resource) => ({
    index(extras = {}) {
      return $axios.$get(`${resource}/`, extras)
    },
  
    show(id, extras = {}) {
      return $axios.$get(`${resource}/${id}/`, extras)
    },
  
    create(payload, extras = {}) {
      return $axios.$post(`${resource}/`, payload, extras)
    },
  
    update(id, payload, extras = {}) {
      return $axios.$patch(`${resource}/${id}/`, payload, extras)
    },
  
    delete(id, extras = {}) {
      return $axios.$delete(`${resource}/${id}/`, extras)
    },
  })
  