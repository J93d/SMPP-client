<h1>Python SMPP Client</h1>

Currently it supports:
  - Bind Receiver
  - Bind Transmitter
  - Bind Transceiver
  - SubmitSM
  - DeliverSM
  - QuerySM
  - ReplaceSM
  - CancelSM
  - Enquire Link

This project will only work in Linux currently. 

The SubmitSM support short as well as long message. It supports UDH, SAR and Payload for sending the message.
The message content can be encoded for 8-bit, Latin(iso-8859-1), Unicode and GSM Encoded. Please make sure to keep the DCS properly.

QuerySM, ReplaceSM and CancelSM requires manual inputs as the message-id of the previous message is required.

Messages and account information can be configured in the xlsx.
It supports automatically sending all messages in sequence. It also supports tcpdump tracing, although it is disabled by default.

I am mainly working on the automated version. The manual version may lag behind or may be discontinued.
