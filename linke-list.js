class Node{
    constructor(value){
        this.value=value;
        this.next=null;
    }
}

class Linklist{
    constructor(){
        this.head=null
        this.size=0
    }

    isEmpty(){
        return this.size===0
    }
    get(){
        return this.size
    }
    prepend(value){
        const node=new Node(value)
        if (this.isEmpty()){
            this.head=node
        }else{
            node.next=this.head
            this.head=node
        }
        this.size++
    }
    print(value){
        let curr=this.head
        let listVlues=''
        while(curr){
            listValues+=`${curr.value}`
            curr=curr.next
        }
    }
}