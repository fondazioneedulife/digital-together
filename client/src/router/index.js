import { createRouter, createWebHistory } from 'vue-router'

import Home from '@/views/Home.vue'
import Course from '@/views/Course.vue'
import CourseView from '@/views/CourseView.vue'
import Opendata from '@/views/Opendata.vue'
import Faq from '@/views/Faq.vue'

const routes = [
  {
    path: '',
    name: 'home',
    component: Home,
    meta:{
      title:'home'
    }
  },
  {
    path: '/corsi',
    name: 'course_list',
    component: Course,
    meta:{
      title:'corsi'
    }
  },
  {
    path: '/corsi/:id',
    name: 'course',
    component: CourseView,
    meta:{
      title:'corsi'
    }

  },
  {
    path: '/opendata',
    name: 'opendata',
    component: Opendata,
    meta:{
      title:'opendata'
    }
  },
  {
    path: '/faq',
    name: 'faq',
    component: Faq,
    meta:{
      title:'faq'
    }
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
    meta:{
      title:'about'
    }
  },
  {
    path:'/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/NotFound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
router.beforeEach((to, from, next) => {
  document.title = 'Digital together | ' + to.meta.title;
  next();
});

export default router
