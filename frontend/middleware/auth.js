export default function ({ store, redirect }) {
    return store.dispatch('fetchUserProfile').then(() => {
        if (!store.state.authenticated) {
            return redirect('/add-token')
        }
    })
}