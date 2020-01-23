import Foo_A from './Component_A'

function InitialFoo_B() {
    console.log('foo1')
}
function Foo_B() {
    Component_A()
    InitialFoo_B()
    console.log('foo1')
}

module.exports = Foo_B;