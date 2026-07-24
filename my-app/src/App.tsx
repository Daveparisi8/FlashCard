// This is the primary landing component for users

import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <section>Header</section>

      <section id="center">
        <p>This is the dynamic landing page for all components</p>
      </section>

      <section id="spacer"></section>

      <section>Footer section</section>
    </>
  )
}

export default App
