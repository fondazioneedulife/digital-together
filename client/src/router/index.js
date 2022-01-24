import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

import Course from '@/views/Course.vue'
import CourseView from '@/views/CourseView.vue'
import Contact from '@/views/Contact.vue'
import Faq from '@/views/Faq.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/corsi',
    name: 'Courses',
    component: Course
  },
  {
    path: '/corsi/:id',
    name: 'Course',
    component: CourseView
  },
  {
    path: '/contatti',
    name: 'Contact',
    component: Contact
  },
  {
    path: '/faq',
    name: 'Faq',
    component: Faq
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
