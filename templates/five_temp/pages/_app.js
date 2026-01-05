import '../../styles/globals.css'
import Head from 'next/head'
import Header from '../../Components/Header'

function MyApp({ Component, pageProps }) {
  return (
    <>
    <Head>
      <title>Nascimento Portfolio</title>
    </Head> 
    <Header />
    <Component {...pageProps} />
    </>
  )
}

export default MyApp
