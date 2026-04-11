import './Header.scss'
import logoImage from '@/assets/images/logo.png'
import clsx from 'clsx'
import {useState} from 'react'

function Header() {

    const isLogin = false

    const menuItems = [
        {label: 'Главная', href: '/'},
        {label: 'Поиск', href: '#!'},
        {label: 'Сообщения', href: '#!'},
    ]

    const url = window.location.pathname

    const [isActive, setIsActive] = useState(false)

    const burgerButtonClick = () => setIsActive(!isActive)

    return (
        <header className="header">
            <div className="header__inner container">
                <div className="header__logo">
                    <a href="/">
                        <img className="header__logo-img" src={logoImage} alt="logo" loading="lazy"/>
                    </a>
                </div>
                <div className={clsx('header__overlay', {'is-active': isActive})}>
                    <nav className="header__menu">
                        <ul className="header__menu-list">
                            {menuItems.map(({label, href}) => (
                                <li className="header__menu-item" key={label}>
                                    <a
                                        className={clsx(
                                            'header__menu-link',
                                            href === url && 'is-active'
                                        )}
                                        href={href}
                                    >
                                        {label}
                                    </a>
                                </li>
                            ))}
                        </ul>
                    </nav>
                    <nav className="header__-menu">
                        <ul className='header__menu-list'>
                            <li className='header__menu-item'>
                                <a className='header__menu-link auth' href="#!">Вход</a>
                            </li>
                            <li className='header__menu-item'>
                                <a className='header__menu-link auth' href="#!">Регистрация</a>
                            </li>
                            <li className='header__menu-item'>
                                <a className='header__menu-link auth' href="#!">Профиль</a>
                            </li>
                        </ul>
                    </nav>
                </div>
                <button className={clsx('header__burger-button burger-button', {'is-active': isActive})}
                        type="button"
                        aria-label="open menu"
                        title="Open menu"
                        onClick={burgerButtonClick}
                >
                    <span className="burger-button__line"></span>
                    <span className="burger-button__line"></span>
                    <span className="burger-button__line"></span>
                </button>
            </div>
        </header>
    )
}

export default Header

