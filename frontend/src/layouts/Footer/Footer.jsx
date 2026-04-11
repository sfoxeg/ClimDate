import './Footer.scss'


function Footer() {
    const currentYear = new Date().getFullYear()
    return (
        <footer className="footer">
            <div className="footer__inner container">
                <div className="footer__body">

                </div>
                <div className="footer__extra">
                    <div className="footer__copyright">
                        © <time dateTime={currentYear}>{currentYear}</time> ClimDate. Powered by&nbsp;
                        <a href="/" target="_blank">Sega</a>
                    </div>
                </div>
            </div>
        </footer>

    )
}

export default Footer