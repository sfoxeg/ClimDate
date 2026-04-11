import './Content.scss'

export default (props) => {
    const {children} = props

    return <main className="content">
        <h1>Test</h1>
        {children}</main>
}