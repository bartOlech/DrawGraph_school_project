import Foo_B from './Component_B'

function InitialFoo_A() {
    console.log('value')
}
function Foo_A() {
    initialFoo()
    Component_B()
    console.log('value')
}

module.exports = Foo_A;