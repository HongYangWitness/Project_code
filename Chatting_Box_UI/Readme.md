# Android_Chatting_Box_UI

This is a simple demo of the UI implementation of Chatting Box by **Android**. This project is an example of 《第一行代码》 Chapter 3.

The result is look like as follows:

![Image text](https://github.com/HongYangWitness/Picture/blob/master/chatting_box_1.jpg)

![Image text](https://github.com/HongYangWitness/Picture/blob/master/chatting_box_@.png)

**How to do:**

+ First, define a Listview, a input line(textview) and a Button
+ Second, define the layout of the list item named msg_item.xml. In this layout file we define the **layout_left**(to represent the message we received) and **layout_right**(sent) using the **nine-patch** png. (define to layout but only use one each time)
+ Then, define a class named Msg that have two attributes:content and **type**(received or sent).
+ Next, define a MessageAdpater, remember when the message is received type, set **rightLayout =view. gone and leftLayout = view.Visible**,vice versa.
+ Finally, define the function of the main_activity, notice the using of  **adapter.notifyDataSetChanged();** (to update the UI) and **msgListView.setSelection(msgList.size());**(to locate the last item of the listview to the top of the UI).

**What I have learnt:**

+ How to use Nine-Patch to let the picture resize the way we want it
+ How to update the UI using Adapter
+ How to implement a chatting box UI