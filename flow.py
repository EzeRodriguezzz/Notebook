########################################## INICIO Confirmar visita 48 hs antes MX ####################################################

confirm_booking_48_hours_before = create_task_flow(name="Confirmar visita 48 hs antes", subtype=CONFIRM_BOOKING_48_HOURS_BEFORE, countries=["MX"])

initial_state = create_task_state(
    key=CONFIRM_BOOKING_48_HOURS_BEFORE,
    name="Enviar recordatorio WA Alianza",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Contestó la llamada?"
    ),
)
confirm_booking_48_hours_before.initial_state_id=initial_state.id
confirm_booking_48_hours_before.save()

#### Inicio Vertical No contestó
# State No contestó
state_no_reply = create_option_state(
    key="no_reply",
    name="No contestó",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Enviar WA de confirmación
state_send_whatsapp_for_confirmation = create_option_state(
    key=SEND_CONFIRMATION_WHATSAPP,
    name="Enviar whatsapp de confirmación",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Se envió el Whatsapp?"
    )
)

# State No se envió WA
state_whatsapp_not_sent = create_option_state(
    key="whatsapp_not_sent",
    name="No se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Se envió WA
state_whatsapp_sent = create_option_state(
    key="whatsapp_sent",
    name="Se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# Edge inicial a No contestó
edge_0 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_no_reply,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre Enviar WA de confirmación y Se envió WA
edge_1 = Edge.objects.create(
    from_state=state_send_whatsapp_for_confirmation,
    to_state=state_whatsapp_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre Enviar WA de confirmación y No se envió WA
edge_2 = Edge.objects.create(
    from_state=state_send_whatsapp_for_confirmation,
    to_state=state_whatsapp_not_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=1,
)

# Edge de vuelta entre No se envió WA y Enviar WA de confirmación
edge_3 = Edge.objects.create(
    from_state=state_whatsapp_not_sent,
    to_state=state_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=1,
)











#### Inicio Vertical Contestó
# State Contestó
state_replied = create_option_state(
    key="contesto",
    name="Contestó",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Quiere confirmar la visita?"
    )
)

# State No contestó
state_could_not_talk = create_option_state(
    key="could_not_talk",
    name="No podía hablar",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State No contestó
state_visit_canceled = create_option_state(
    key="visit_canceled",
    name="Canceló visita",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State No contestó
state_visit_confirmed = create_option_state(
    key="visit_confirmed",
    name="Confirmó visita",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

########################################## FIN Confirmar visita 48 hs antes MX ####################################################