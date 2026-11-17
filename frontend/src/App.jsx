import { useEffect, useState } from 'react'
import { Link, NavLink, Route, Routes, useNavigate } from 'react-router-dom'
import './App.scss'

const API = (import.meta.env.VITE_API_URL || 'http://localhost:8000').replace(/\/$/, '')
const API_V1 = `${API}/api/v1`

async function request(path, options = {}) {
    const response = await fetch(`${API_V1}${path}`, options)
    const payload = await response.json().catch(() => ({}))
    if (!response.ok) throw new Error(payload.detail || 'Не удалось выполнить запрос. Попробуйте ещё раз.')
    return payload
}

function Brand({ light = false }) {
    return <Link className={`brand ${light ? 'brand--light' : ''}`} to="/" aria-label="ClimDate — главная">
        <span className="brand__mark">c<span>.</span></span><span className="brand__name">climdate</span>
    </Link>
}

function Header() {
    const [menuOpen, setMenuOpen] = useState(false)
    const close = () => setMenuOpen(false)
    return <header className="site-header"><div className="container header-inner">
        <Brand />
        <button className="menu-toggle" onClick={() => setMenuOpen(!menuOpen)} aria-label="Открыть меню" aria-expanded={menuOpen}><span /><span /><span /></button>
        <nav className={`main-nav ${menuOpen ? 'main-nav--open' : ''}`}>
            <NavLink to="/" onClick={close}>Главная</NavLink><a href="/#about" onClick={close}>О проекте</a><NavLink to="/search" onClick={close}>Сообщество</NavLink>
            <div className="nav-actions"><NavLink className="button button--quiet" to="/login" onClick={close}>Войти</NavLink><NavLink className="button button--primary button--small" to="/register" onClick={close}>Присоединиться</NavLink></div>
        </nav>
    </div></header>
}

function Footer() {
    return <footer className="site-footer"><div className="container footer-inner"><Brand light /><span>Находим людей, с которыми хочется выше.</span><span>© {new Date().getFullYear()} ClimDate</span></div></footer>
}

function Home() {
    const [cities, setCities] = useState([])
    const [citiesError, setCitiesError] = useState('')
    useEffect(() => { request('/cities').then(setCities).catch(() => setCitiesError('Города пока не загрузились')) }, [])
    return <>
        <section className="hero"><div className="container hero-grid"><div className="hero-copy">
            <span className="eyebrow"><i /> СООБЩЕСТВО ЛЮБИТЕЛЕЙ СКАЛОЛАЗАНИЯ</span>
            <h1>Твоя следующая<br /><em>вершина</em> — это люди.</h1>
            <p className="hero-lead">ClimDate помогает найти компанию для скалодрома, напарников для выездов и тех, кто разделяет твою любовь к горам.</p>
            <div className="hero-actions"><Link className="button button--primary" to="/register">Найти свою компанию <span>↗</span></Link><a className="text-link" href="#about">Узнать о проекте <span>↓</span></a></div>
            <div className="hero-note"><div className="avatar-stack"><b>А</b><b>М</b><b>К</b></div><span>Знакомства начинаются<br />с общего маршрута</span></div>
        </div><div className="hero-art" aria-label="Иллюстрация скалолазания"><div className="art-sun" /><div className="art-tag art-tag--top">FIND YOUR CLIMBING CREW</div><div className="cliff cliff--back" /><div className="cliff cliff--front" /><div className="climber"><span className="climber-head" /><span className="climber-body" /><span className="climber-arm" /><span className="climber-leg" /></div><div className="art-tag art-tag--bottom"><span>↗</span> ВЫШЕ ВМЕСТЕ</div><span className="art-coordinate">55°45' N&nbsp; 37°37' E</span></div></div>
        <div className="hero-bottom container"><span>01 / ЗНАКОМЬСЯ</span><span>02 / ОБЪЕДИНЯЙСЯ</span><span>03 / ПОКОРЯЙ</span></div></section>
        <section className="intro section" id="about"><div className="container intro-grid"><div><span className="eyebrow">БОЛЬШЕ, ЧЕМ СПОРТ</span><h2>Лучшие истории<br />случаются <em>вместе.</em></h2></div><div className="intro-text"><p>Иногда не хватает одного человека, чтобы решиться на новый маршрут. Или компании, которая поймёт, почему ты снова проводишь выходные на стене.</p><p>Мы создаём пространство, где легко встретить своих — независимо от опыта и уровня подготовки.</p></div></div></section>
        <section className="features section"><div className="container"><div className="section-heading"><div><span className="eyebrow">ТВОЙ МАРШРУТ НАЧИНАЕТСЯ ЗДЕСЬ</span><h2>Найди <em>своих.</em></h2></div><span className="section-index">01 — 03</span></div><div className="feature-grid">
            <article className="feature-card"><span className="feature-number">01</span><div className="feature-icon">↗</div><h3>Знакомься</h3><p>Встречай людей, которым так же нравится движение вверх, как и тебе.</p></article>
            <article className="feature-card feature-card--accent"><span className="feature-number">02</span><div className="feature-icon">⌁</div><h3>Собирай команду</h3><p>Ищи напарников для тренировок, боулдеринга и поездок на скалы.</p></article>
            <article className="feature-card"><span className="feature-number">03</span><div className="feature-icon">⛰</div><h3>Открывай новое</h3><p>Пробуй новые места и маршруты вместе с близкими по духу людьми.</p></article>
        </div></div></section>
        <section className="cities-section section"><div className="container cities-inner"><div><span className="eyebrow">ГЕОГРАФИЯ CLIMDATE</span><h2>Откуда<br /><em>начнём?</em></h2><p>Выбирай свой город и ищи компанию рядом.</p><Link className="text-link" to="/search">Смотреть сообщество <span>↗</span></Link></div><div className="city-panel"><div className="city-panel__top"><span>ГОРОДА СООБЩЕСТВА</span><span>LIVE</span></div>{cities.length ? cities.slice(0, 5).map((city, index) => <div className="city-row" key={city.id}><span className="city-row__number">0{index + 1}</span><strong>{city.name}</strong><span>↗</span></div>) : <div className="city-empty">{citiesError || 'Список городов скоро появится. А пока можно присоединиться к нам.'}</div>}<Link to="/register" className="city-panel__join">ТВОЙ ГОРОД МОЖЕТ БЫТЬ СЛЕДУЮЩИМ ↗</Link></div></div></section>
        <section className="cta-section"><div className="container cta-inner"><span className="eyebrow">ТВОЯ КОМАНДА УЖЕ ГДЕ-ТО РЯДОМ</span><h2>Пойдём <em>выше?</em></h2><Link className="button button--dark" to="/register">Создать аккаунт <span>↗</span></Link></div></section>
    </>
}

function AuthPage({ mode }) {
    const isRegister = mode === 'register', navigate = useNavigate()
    const [email, setEmail] = useState(''), [password, setPassword] = useState(''), [busy, setBusy] = useState(false), [error, setError] = useState('')
    async function submit(event) {
        event.preventDefault(); setError(''); setBusy(true)
        try {
            const params = new URLSearchParams({ email, password })
            const result = await request(`/auth/${isRegister ? 'register' : 'login'}`, { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: params })
            if (result.token) { localStorage.setItem('climdate_token', result.token); localStorage.setItem('climdate_email', email); navigate('/profile') }
            else if (isRegister) navigate('/login', { state: { registered: true } })
        } catch (err) { setError(err.message) } finally { setBusy(false) }
    }
    return <main className="auth-page"><div className="auth-aside"><Brand light /><div className="auth-aside__copy"><span className="eyebrow">CLIMDATE COMMUNITY</span><h1>Люди делают<br />подъём <em>легче.</em></h1><p>Найди тех, с кем захочется разделить следующий маршрут.</p></div><span className="auth-aside__foot">FIND YOUR PEOPLE. FIND YOUR CLIMB.</span></div><div className="auth-main"><div className="auth-form-wrap"><Link className="back-link" to="/">← На главную</Link><span className="eyebrow">{isRegister ? 'СТАНЬ ЧАСТЬЮ СООБЩЕСТВА' : 'С РАДОСТЬЮ СНОВА ВИДИМ'}</span><h2>{isRegister ? 'Создать аккаунт' : 'С возвращением'}</h2><p className="auth-description">{isRegister ? 'Пара шагов — и ты ближе к новым знакомствам.' : 'Войди, чтобы продолжить свой путь с ClimDate.'}</p><form onSubmit={submit} className="auth-form"><label htmlFor="email">Электронная почта</label><input id="email" type="email" autoComplete="email" placeholder="you@example.com" value={email} onChange={e => setEmail(e.target.value)} required /><label htmlFor="password">Пароль</label><input id="password" type="password" autoComplete={isRegister ? 'new-password' : 'current-password'} placeholder="Не менее 8 символов" minLength={8} value={password} onChange={e => setPassword(e.target.value)} required />{error && <div className="form-error" role="alert">{error}</div>}<button className="button button--primary auth-submit" disabled={busy}>{busy ? 'Подождите…' : isRegister ? 'Зарегистрироваться ↗' : 'Войти ↗'}</button></form><p className="auth-switch">{isRegister ? 'Уже есть аккаунт?' : 'Впервые с нами?'} <Link to={isRegister ? '/login' : '/register'}>{isRegister ? 'Войти' : 'Создать аккаунт'}</Link></p><p className="auth-legal">Продолжая, ты соглашаешься с правилами сообщества ClimDate.</p></div></div></main>
}

function Profile() {
    const email = localStorage.getItem('climdate_email'), navigate = useNavigate()
    if (!localStorage.getItem('climdate_token')) return <div className="simple-page"><h1>Сначала нужно войти</h1><Link className="button button--primary" to="/login">Войти в аккаунт</Link></div>
    return <div className="simple-page"><span className="eyebrow">ТВОЁ ПРОСТРАНСТВО</span><h1>Привет!</h1><p>{email}</p><p>Профиль будет расширяться по мере развития сообщества.</p><button className="button button--quiet" onClick={() => { localStorage.removeItem('climdate_token'); localStorage.removeItem('climdate_email'); navigate('/') }}>Выйти</button></div>
}
function SearchPage() { return <div className="simple-page"><span className="eyebrow">CLIMDATE COMMUNITY</span><h1>Скоро здесь<br /><em>встретимся.</em></h1><p>Раздел поиска участников появится, когда на бэкенде будет готова выдача профилей.</p><Link className="button button--primary" to="/register">Присоединиться ↗</Link></div> }

export default function App() {
    return <div className="App"><Header /><Routes><Route path="/" element={<Home />} /><Route path="/login" element={<AuthPage mode="login" />} /><Route path="/register" element={<AuthPage mode="register" />} /><Route path="/profile" element={<Profile />} /><Route path="/search" element={<SearchPage />} /><Route path="*" element={<div className="simple-page"><h1>Страница не найдена</h1><Link to="/">На главную</Link></div>} /></Routes><Footer /></div>
}
